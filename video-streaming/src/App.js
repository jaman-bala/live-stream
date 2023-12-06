import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography, Table, TableBody, TableCell, TableRow, Container } from '@mui/material';
import ButtonAppBar from './componets/ButtonAppBar';
import axios from 'axios';

const StreamImageCard = ({ currentStreamId }) => (
  <Card sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: '35px', width: '120vh' }}>
    {currentStreamId && (
      <CardContent>
        <img
          id="streamImage"
          className="img-rounded"
          style={{ maxWidth: '100%' }}
          src={`http://127.0.0.1:8000/streams/${currentStreamId}`}
          alt="Stream"
        />
      </CardContent>
    )}
  </Card>
);

const StreamTableCard = ({ streams, changeStreamImage }) => (
  <Card sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: '40%', mt: '35px', margin: '15px' }}>
    <Table>
      <TableBody>
        {streams.map((stream) => (
          <TableRow key={stream.id}>
            <TableCell>
              <Typography component="a" href="#" onClick={() => changeStreamImage(stream.id)}>
                {stream.title}
              </Typography>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </Card>
);

const App = () => {
  const [streams, setStreams] = useState([]);
  const [currentStreamId, setCurrentStreamId] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/streams/');
        setStreams(response.data);
        // Set the current stream to the first one by default
        setCurrentStreamId(response.data.length > 0 ? response.data[0].id : null);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // Empty dependency array means this effect runs once on mount

  const changeStreamImage = async (streamId) => {
    try {
      await fetch(`http://127.0.0.1:8000/streams/${streamId}`);
      setCurrentStreamId(streamId);
    } catch (error) {
      console.error('Error fetching stream:', error);
    }
  };

  return (
    <div>
      <ButtonAppBar />

      <Container sx={{ display: 'flex' }}>
        {/* Display the current stream image */}
        <StreamImageCard currentStreamId={currentStreamId} />

        {/* Display the list of streams with links to change the current stream */}
        <StreamTableCard streams={streams} changeStreamImage={changeStreamImage} />
      </Container>
    </div>
  );
};

export default App;
