import React, { useState, useEffect } from 'react';
import { getMarks } from './services/api';
import MarksTable from './components/MarksTable';
import AddMarkForm from './components/AddMarkForm';
import { Container, Typography, Box, Avatar } from '@mui/material';
import SchoolIcon from '@mui/icons-material/School';

const App = () => {
  const [marks, setMarks] = useState([]);

  // Fetch marks from the backend
  const fetchMarks = async () => {
    try {
      const response = await getMarks();
      console.log('Fetched marks:', response.data);
      setMarks(response.data || []);
    } catch (error) {
      console.error('Error fetching marks:', error);
    }
  };

  useEffect(() => {
    fetchMarks();
  }, []);

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      {/* Header Section */}
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        sx={{
          mb: 4,
          py: 4,
          backgroundColor: '#f5f5f5',
          borderRadius: 2,
          boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Avatar sx={{ bgcolor: 'primary.main', width: 80, height: 80, mb: 2 }}>
          <SchoolIcon sx={{ fontSize: 40 }} />
        </Avatar>
        <Typography
          variant="h3"
          gutterBottom
          sx={{ fontFamily: "'Poppins', sans-serif", fontWeight: 600 }}
        >
          Exam Marks Tracker
        </Typography>
        <Typography
          variant="subtitle1"
          color="textSecondary"
          sx={{ fontFamily: "'Roboto', sans-serif" }}
        >
          Keep track of your exam marks with ease!
        </Typography>
      </Box>

      {/* Add Mark Form */}
      <AddMarkForm onMarkAdded={fetchMarks} />

      {/* Marks Table */}
      <MarksTable marks={marks} onMarkDeleted={fetchMarks} />
    </Container>
  );
};

export default App;
