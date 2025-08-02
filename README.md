# Electrical Machines Q&A Platform

A comprehensive Django web application for asking and answering questions about electrical machines, powered by AI-generated responses.

## 🚀 Features

- **User Authentication**: Complete registration and login system
- **Question Management**: Ask, browse, and search electrical machine questions
- **AI-Powered Answers**: Integrated ChatGPT API for generating technical answers
- **Categorization**: Organized by electrical machine types (DC Motors, AC Motors, Transformers, etc.)
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Admin Panel**: Django admin interface for content management
- **Search & Filter**: Advanced search and category filtering
- **User Profiles**: Extended user profiles with expertise levels

## 📋 Requirements

- Python 3.8 or higher
- MySQL 8.0 or higher
- Git
- Virtual environment 

## 🛠 Quick Setup

1. **Extract the project files** 
2. **Navigate to project directory**
   ```bash
   cd electrical_machines_qa
   ```

3. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up MySQL database**
   - Create database: `electrical_machines_qa`
   - Update `.env` file with your database credentials

6. **Configure environment variables**
   - Edit `.env` file with your settings
   - Add your OpenAI API key for AI features

7. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Load sample data (optional)**
   ```bash
   python manage.py populate_sample_data
   ```

10. **Run development server**
    ```bash
    python manage.py runserver
    ```

Visit `http://localhost:8000` to see the application.

## 🔧 Configuration

### Environment Variables (.env)

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=electrical_machines_qa
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
OPENAI_API_KEY=your-openai-api-key
```

### OpenAI API Setup

1. Sign up for an OpenAI account
2. Generate an API key
3. Add the key to your `.env` file
4. Ensure you have sufficient credits for API usage

## 📝 Usage

### For Users
1. **Register**: Create an account to ask questions
2. **Ask Questions**: Use the "Ask Question" form with appropriate categories
3. **Browse**: Search and filter questions by category
4. **View Answers**: AI-generated answers appear automatically

### For Administrators
1. Access Django admin at `/admin/`
2. Manage users, questions, and answers
3. Monitor system usage and performance

## 🗄️ Database Schema

### Key Models
- **Question**: Stores user questions with categories (5 fields)
- **Answer**: AI-generated answers linked to questions (5 fields)
- **UserProfile**: Extended user information (5 fields)
- **QuestionView**: Analytics for question views (5 fields)

## 🚀 Production Deployment

For Ubuntu server deployment, use the provided deployment scripts in the `deployment/` directory.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the documentation
- Review the troubleshooting section
- Create an issue in the repository

## 🙏 Acknowledgments

- Django framework and community
- OpenAI for API integration
- Bootstrap for UI components
