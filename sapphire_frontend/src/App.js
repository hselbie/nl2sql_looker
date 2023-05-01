import './App.css';

import * as React from 'react';
import { useRef, useState } from 'react';

import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import TextField from '@mui/material/TextField';
import Fab from '@mui/material/Fab';
import InputAdornment from '@mui/material/InputAdornment';
import SendIcon from '@mui/icons-material/Send';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Unstable_Grid2';
import Iframe from 'react-iframe'
import Stack from '@mui/joy/Stack';

import CircularProgress from '@mui/material/CircularProgress';

const exampleSearchText = 'Enter a prompt here';

const exampleResponse = {
  results: ["company a", "company b", "etc"],
  llm_text: "The customer with the top average sales this year is Standard Retail. Their average sales were $13.5 million. This is significantly higher than the average sales of any other customer. Standard Retail is a large and well-established company, and their sales are likely to continue to be high in the future. ",
  context: ["Which customer has the top sales this year?"]
};
const exampleQuestion = 'Which customer has the top sales this year?';

const llmUrl = '/query';

let entityData = null;


const App = props => {
  const [questionDisplay, setQuestionDisplay] = useState(null);
  const [question, setQuestion] = useState(exampleQuestion);
  const [answer, setAnswer] = useState(null);
  const [lookerUrl, setLookerUrl] = useState(null);
  const [frameHeight, setFrameHeight] = useState('100px');
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit (event) {
    event.preventDefault();
    setIsLoading(true);

    if (entityData) {
      console.log(JSON.stringify(entityData));
    }
    setFrameHeight('1800px');

    setQuestionDisplay('Q: ' + question);

    //const request = new Request(llmUrl + "?question="+question, {
    const request = new Request(llmUrl, {
      method: 'POST',
      body: JSON.stringify({"question": question, "entities": entityData}),
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
    });

    // send query to LLM api
    fetch(request)
    .then(response => { return response.json();})
      .then((responseData) => {
        const data = responseData;
        setAnswer(data.llm_text);
        setLookerUrl(data.looker_url);
        //setEntities(data.entities);
        entityData = data.entities;
        setIsLoading(false);
        //console.log(data.entities);
    });
  }

  function handleQuestionChange(e) {
    setQuestion(e.target.value);
  }

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <CssBaseline />
      <Stack className="content">
      <Container component="main" sx={{ mt: 8, mb: 2 }} maxWidth="md">
        <Typography variant="h2" component="h1" gutterBottom>
          Cortex with GenAI Demo
        </Typography>
        <Typography variant="h5" component="h5" gutterBottom>
          {questionDisplay}
        </Typography>
        <Typography variant="body2" color="text" sx={{ mt: 3, mb: 3 }}>
          {answer}
        </Typography>
        {isLoading && <CircularProgress />}
        <iframe src={lookerUrl} height={frameHeight} scrolling="no" />
        
      </Container>
      <Box
        component="footer"
        sx={{
          py: 3,
          px: 2,
          mt: 'auto',
          backgroundColor: (theme) =>
            theme.palette.mode === 'light'
              ? theme.palette.grey[200]
              : theme.palette.grey[800],
        }}
      >
        <Container maxWidth="md">
          <form onSubmit={handleSubmit}>
            <Box sx={{ display: 'flex', alignItems: 'flex-end' }}>
              <TextField fullWidth label={exampleSearchText} id="promptField" onChange={handleQuestionChange} value={question} />
              <button>
                <Fab color="primary" aria-label="Send" sx={{ ml: 3 }}>
                  <SendIcon />
                </Fab>
              </button>
            </Box>
          </form>
          <Typography variant="body2" color="text.secondary" sx={{ mt: 3 }}>
            Made by Google Cloud for SAP customers
          </Typography>
        </Container>
      </Box>
      </Stack>
    </Box>
  );
}

export default App;
