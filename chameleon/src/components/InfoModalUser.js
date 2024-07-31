import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const buttonStyle = {
  color: '#61dafb',
  fontSize: '1.1em',
  paddingBottom: '10px',
  margin: '0',
  fontWeight: 100,
  textTransform: 'none', // This removes capitalization
};

const steps = [
  { title: 'Step 1', content: "Open the website you're interested in your web browser" },
  { title: 'Step 2', content: 'Right-click anywhere on the page and select “Inspect” from the menu' },
  { title: 'Step 3', content: 'This will open the HTML code for the page. Select and copy the HTML code you want to work on' },
  { title: 'Step 4', content: 'Paste the HTML code into the area provided, and wait for Chameleon to take effect!' }
];

export default function MultiStepModal() {
  const [open, setOpen] = useState(false);
  const [stepIndex, setStepIndex] = useState(0);

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleNext = () => {
    if (stepIndex < steps.length - 1) {
      setStepIndex(stepIndex + 1);
    }
  };

  const handleBack = () => {
    if (stepIndex > 0) {
      setStepIndex(stepIndex - 1);
    }
  };

  return (
    <div>
      <Button onClick={handleOpen} sx={buttonStyle}>Input</Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="multi-step-modal-title"
        aria-describedby="multi-step-modal-description"
      >
        <Box sx={style}>
          <Typography id="multi-step-modal-title" variant="h6" component="h2">
            {steps[stepIndex].title}
          </Typography>
          <Typography id="multi-step-modal-description" sx={{ mt: 2 }}>
            {steps[stepIndex].content}
          </Typography>
          <Box sx={{ mt: 2 }}>
            <Button
              onClick={handleBack}
              disabled={stepIndex === 0}
              sx={buttonStyle}
            >
              Back
            </Button>
            <Button
              onClick={handleNext}
              disabled={stepIndex === steps.length - 1}
              sx={buttonStyle}
            >
              Next
            </Button>
          </Box>
        </Box>
      </Modal>
    </div>
  );
}
