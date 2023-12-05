import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const NavBar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          UNAA ONLINE
        </Typography>
        <Button color="inherit">About</Button>
        {/* Add more buttons as needed */}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
