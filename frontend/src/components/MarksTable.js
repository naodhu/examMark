import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Button,
  Snackbar,
  Alert,
} from '@mui/material';
import { deleteMark } from '../services/api';

const MarksTable = ({ marks, onMarkDeleted }) => {
  const [snackbar, setSnackbar] = useState({
    open: false,
    message: '',
    severity: 'success',
  });

  const handleSnackbarClose = () => {
    setSnackbar({ ...snackbar, open: false });
  };

  const handleDelete = async (assessmentName) => {
    try {
      await deleteMark(assessmentName);
      setSnackbar({
        open: true,
        message: 'Mark deleted successfully!',
        severity: 'success',
      });
      onMarkDeleted();
    } catch (error) {
      console.error('Error deleting mark:', error);
      setSnackbar({
        open: true,
        message: 'Failed to delete the mark. Please try again.',
        severity: 'error',
      });
    }
  };

  const groupedMarks = marks.reduce((acc, mark) => {
    const unit = mark[0];
    if (!acc[unit]) acc[unit] = [];
    acc[unit].push(mark);
    return acc;
  }, {});

  return (
    <TableContainer component={Paper} sx={{ mt: 4, p: 2 }}>
      <Typography variant="h5" align="center" gutterBottom>
        Marks List
      </Typography>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Unit Name</TableCell>
            <TableCell>Assessment Name</TableCell>
            <TableCell>Raw Score</TableCell>
            <TableCell>Weight (%)</TableCell>
            <TableCell>Adjusted Mark</TableCell>
            <TableCell>Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {Object.keys(groupedMarks).map((unit) => (
            <React.Fragment key={unit}>
              <TableRow>
                <TableCell colSpan={6}>
                  <Typography variant="h6">{unit}</Typography>
                </TableCell>
              </TableRow>
              {groupedMarks[unit].map((mark, index) => (
                <TableRow key={index}>
                  <TableCell>{mark[0]}</TableCell>
                  <TableCell>{mark[1]}</TableCell>
                  <TableCell>{mark[2]}</TableCell>
                  <TableCell>{mark[3]}</TableCell>
                  <TableCell>{mark[4]}</TableCell>
                  <TableCell>
                    <Button
                      variant="contained"
                      color="secondary"
                      size="small"
                      onClick={() => handleDelete(mark[1])}
                    >
                      Delete
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </React.Fragment>
          ))}
        </TableBody>
      </Table>

      {/* Snackbar for Notifications */}
      <Snackbar
        open={snackbar.open}
        autoHideDuration={3000}
        onClose={handleSnackbarClose}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        <Alert onClose={handleSnackbarClose} severity={snackbar.severity}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </TableContainer>
  );
};

export default MarksTable;
