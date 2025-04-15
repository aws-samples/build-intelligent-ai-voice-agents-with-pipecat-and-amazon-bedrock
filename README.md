# Building Intelligent Voice AI Agents with Pipecat and Amazon Bedrock

This repo shows you how to build real-time, voice-enabled AI agents using a fork of the open-source [Pipecat](https://github.com/adithyaxx/pipecat/tree/add-bedrock-support) framework (and [Pipecat Flows](https://github.com/adithyaxx/pipecat-flows/tree/add-bedrock-support)) and Amazon Bedrock foundation models. These forks contain support for Amazon Bedrock models with open PRs to the source repos.

## Overview

The following diagram illustrates the high-level architecture of this solution:

![](assets/diagram.png)

Key components include:
- Daily WebRTC streaming, VAD, noise suppression
- Amazon Transcribe (STT) + Bedrock + Amazon Polly (TTS)
- Pipecat Flows for dialog management and task execution

Built by AWS Generative AI Innovation Center. Ideal for anyone looking to quickly prototype voice AI agents for various use cases.

## Quick Start

### First, start the bot server:

1. Navigate to the server directory:
   ```bash
   cd server
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Update keys in .env:
    ```ini
    DAILY_API_KEY=XXXX
    AWS_ACCESS_KEY_ID=XXXX
    AWS_SECRET_ACCESS_KEY=XXXX
    AWS_SESSION_TOKEN=XXXX
    AWS_REGION=XXXX
     ```
5. Start the server:
   ```bash
   python server.py
   ```

### Next, connect using the prebuilt client app:

1. Visit http://localhost:7860

2. Allow microphone access when prompted

3. Wait for the bot to speak

## Requirements

- Python 3.10+
- Daily API key
- AWS Access keys
- Modern web browser with WebRTC support

## Project Structure

```
pipecat-voice-agent/
├── server/              # Bot server implementation
│   ├── bot.py/          # Pipecat pipeline implementation
│   ├── flow.py/         # Pipecat flow config
│   ├── server.py        # FastAPI server
│   └── requirements.txt
```

## Contributors

- [Adithya Suresh](https://www.linkedin.com/in/adithyaxx/) - Deep Learning Architect, AWS Generative AI Innovation Center
- [Daniel Wirjo](https://www.linkedin.com/in/wirjo/) - Senior Solutions Architect, AWS Generative AI Startups

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
