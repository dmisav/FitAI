# FitAI Trainer

Your AI-powered personal fitness coach that generates personalized workout plans, nutrition advice, and fitness guidance using GitHub Models.

## Features

- 🤖 **AI-Powered Coaching**: Get personalized fitness advice from advanced AI models
- 💪 **Custom Workout Plans**: Tailored exercises based on your goals and fitness level
- 🎯 **Goal-Oriented**: Focus on weight loss, muscle building, cardio, flexibility, and more
- 📱 **Modern UI**: Beautiful, responsive interface with fitness-themed design
- ⚡ **Quick Suggestions**: Pre-built templates for common fitness goals
- 🔒 **Safe & Reliable**: Built with safety and proper form in mind

## Getting Started

### Prerequisites

- Python 3.8 or higher
- GitHub Models API access
- GitHub token with appropriate permissions

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd FitAI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
GITHUB_TOKEN=your_github_token_here
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Describe Your Goals**: Tell FitAI about your fitness objectives, current level, available time, and equipment access
2. **Get Personalized Plan**: Receive a detailed workout plan tailored to your needs
3. **Follow & Progress**: Use the generated plan to achieve your fitness goals

### Example Inputs

- "I'm a beginner looking to lose 20 pounds and build muscle. I have 3 days a week to work out and access to a gym."
- "I want to improve my cardiovascular fitness and can work out 4 times a week at home with minimal equipment."
- "I'm training for a marathon and need a structured running plan with cross-training."

## Configuration

The application uses a `.prompt.yml` file to configure the AI model behavior. You can customize:

- **System Prompt**: The AI's role and expertise
- **Model**: The GitHub Model to use (default: openai/gpt-4.1)
- **Temperature**: Creativity level (0.0-1.0)

## Deployment

### Heroku

1. Create a Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git:
```bash
heroku create your-fitai-app
git push heroku main
```

### Other Platforms

The application includes a `Procfile` for easy deployment to various platforms that support Python web applications.

## Technology Stack

- **Backend**: Flask (Python)
- **AI Models**: GitHub Models API
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Icons**: Font Awesome
- **Styling**: Custom CSS with fitness-themed design

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository.

---

**Built with ❤️ and powered by GitHub Models** 