import React, { useState } from 'react';
import {
  TextField,
  Button,
  Card,
  CardContent,
  Typography,
  Grid,
} from '@mui/material';
import { addMark } from '../services/api';

const AddMarkForm = ({ onMarkAdded }) => {
  const [formData, setFormData] = useState({
    unit_name: '',
    assessment_name: '',
    raw_score: '',
    percentage_weight: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { raw_score, percentage_weight } = formData;
    const [score, total] = raw_score.split('/').map(Number);
    const adjusted_mark = ((score / total) * percentage_weight).toFixed(2);

    try {
      await addMark({ ...formData, adjusted_mark });
      onMarkAdded();
      setFormData({
        unit_name: '',
        assessment_name: '',
        raw_score: '',
        percentage_weight: '',
      });
      alert('Mark added successfully!');
    } catch (error) {
      console.error('Error adding mark:', error);
    }
  };

  return (
    <Card sx={{ mb: 4 }}>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          Add New Mark
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                label="Unit Name"
                name="unit_name"
                value={formData.unit_name}
                onChange={handleChange}
                fullWidth
                required
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                label="Assessment Name"
                name="assessment_name"
                value={formData.assessment_name}
                onChange={handleChange}
                fullWidth
                required
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                label="Raw Score (e.g., 40/50)"
                name="raw_score"
                value={formData.raw_score}
                onChange={handleChange}
                fullWidth
                required
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                label="Weight (%)"
                name="percentage_weight"
                value={formData.percentage_weight}
                onChange={handleChange}
                type="number"
                fullWidth
                required
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            variant="contained"
            color="primary"
            sx={{ mt: 2 }}
          >
            Add Mark
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};

export default AddMarkForm;
