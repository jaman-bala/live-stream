import React, { useState } from 'react';

const VideoStream = ({ rtspUrl }) => {
   const [currentStreamId, setCurrentStreamId] = useState(1);
  
   const changeStream = (streamId) => {
     setCurrentStreamId(streamId);
   };
  
   return (
     <div>
       <img src={`http://127.0.0.1:8000/streams/${currentStreamId}`} alt="Stream" />
       <button onClick={() => changeStream(2)}>Change Stream</button>
     </div>
   );
  };

export default VideoStream;
