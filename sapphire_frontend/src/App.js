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

const exampleSearchText = 'Enter a prompt here';

const exampleResponse = {
  results: ["company a", "company b", "etc"],
  llm_text: "The customer with the top average sales this year is Standard Retail. Their average sales were $13.5 million. This is significantly higher than the average sales of any other customer. Standard Retail is a large and well-established company, and their sales are likely to continue to be high in the future. ",
  context: ["Which customer has the top sales this year?"]
};
const exampleQuestion = 'Which customer has the top sales this year?';
const exampleLookerUrl = 'https://cortexqa.cloud.looker.com/login/embed/%2Fembed%2Fdashboards%2F61%3FYear%3D2022%252F10%252F01%2Bto%2B2023%252F03%252F31%26Currency%3DUSD%26Region%3D%26Sales%2BOrg%3D%26Distribution%2BChannel%3D%26Division%3D%26Product%3D%26Customer%3D?permissions=%5B%22access_data%22%2C%22see_lookml_dashboards%22%2C%22see_looks%22%2C%22see_user_dashboards%22%2C%22explore%22%2C%22create_table_calculations%22%2C%22create_custom_fields%22%2C%22can_create_forecast%22%2C%22save_content%22%2C%22create_public_looks%22%2C%22download_with_limit%22%2C%22download_without_limit%22%2C%22schedule_look_emails%22%2C%22schedule_external_look_emails%22%2C%22create_alerts%22%2C%22follow_alerts%22%2C%22send_to_s3%22%2C%22send_to_sftp%22%2C%22send_outgoing_webhook%22%2C%22send_to_integration%22%2C%22see_sql%22%2C%22see_lookml%22%2C%22develop%22%2C%22deploy%22%2C%22support_access_toggle%22%2C%22use_sql_runner%22%2C%22clear_cache_refresh%22%2C%22see_drill_overlay%22%2C%22manage_spaces%22%2C%22manage_homepage%22%2C%22manage_models%22%2C%22create_prefetches%22%2C%22login_special_email%22%2C%22embed_browse_spaces%22%2C%22embed_save_shared_space%22%2C%22see_alerts%22%2C%22see_queries%22%2C%22see_logs%22%2C%22see_users%22%2C%22sudo%22%2C%22see_schedules%22%2C%22see_pdts%22%2C%22see_datagroups%22%2C%22update_datagroups%22%2C%22see_system_activity%22%2C%22mobile_app_access%22%5D&models=%5B%22All%22%5D&signature=G6eYktIdMVDEfmGAH5VeMdc%2BLVs%3D&nonce=%22df4ee97bdaf7088cad87785364538f98%22&time=1682548061&session_length=900&external_user_id=%223%22&access_filters=%7B%7D&first_name=%22Sanjay%22&last_name=%22Agravat%22&group_ids=%5B%225%22%5D&external_group_id=%22Sapphire_Test_Space%22&user_attributes=%7B%22region%22%3A%22New+York%22%2C%22country%22%3A%22USA%22%7D&force_logout_login=false&print_mode=true';

const llmUrl = 'example.com';

const App = props => {
  const [questionDisplay, setQuestionDisplay] = useState(null);
  const [question, setQuestion] = useState(exampleQuestion);
  const [answer, setAnswer] = useState(null);
  const [lookerUrl, setLookerUrl] = useState(null);
  const [frameHeight, setFrameHeight] = useState('100px');

  async function handleSubmit (event) {
    event.preventDefault();

    setFrameHeight('1800px');

    setQuestionDisplay('Q: ' + question);

    const request = new Request(llmUrl, {
      method: 'POST',
      body: ''
    });

    // send query to LLM api
    /*
    fetch(request)
      .then((response) => {
        const data = response.json();
        setAnswer(data.llm_text);
        setLookerUrl(data.looker_url);
    });
    */
    setAnswer(exampleResponse.llm_text);
    setLookerUrl(exampleLookerUrl);
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
          Welcome to the Sapphire LLM!
        </Typography>
        <Typography variant="h5" component="h5" gutterBottom>
          {questionDisplay}
        </Typography>
        <Typography variant="body2" color="text" sx={{ mt: 3, mb: 3 }}>
          {answer}
        </Typography>
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
