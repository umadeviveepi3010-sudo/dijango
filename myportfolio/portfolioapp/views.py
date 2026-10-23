from django.shortcuts import render


def home(request):
    context = {
        'name': 'Umadevi Veepi',
        'headline': 'Motivated Full-stack Developer and Web Designer',
        'summary': (
            'I am a B.E. Computer Science Engineering student building interactive, '
            'user-friendly web applications with Python, SQL, C language, and modern front-end design. '
            'I combine problem-solving with data-driven thinking to deliver polished product-ready solutions.'
        ),
        'short_summary': 'B.E. student building clean web experiences with Python, C, and modern UI design.',
        'stats': [
            {'value': '6+', 'label': 'Certifications'},
            {'value': '3+', 'label': 'Projects'},
            {'value': '2023-27', 'label': 'B.E. in progress'},
        ],
        'skills': [
            'Python',
            'SQL',
            'C language',
            'Data Science',
            'HTML/CSS/JavaScript',
            'Web Design',
            'Machine Learning',
            'Data Visualization',
        ],
        'languages': [
            'English',
            'Telugu',
            'Hindi',
        ],
        'projects': [
            {
                'title': 'AirGuard',
                'description': 'AI-powered AQI prediction for major Indian cities with data analytics and visualization.',
                'tags': ['Python', 'Machine Learning', 'Data Analytics', 'Predictive Modeling'],
            },
            {
                'title': 'SmartWeb',
                'description': 'Responsive website design project built with HTML, CSS, and JavaScript for modern browsing experiences.',
                'tags': ['HTML', 'CSS', 'JavaScript', 'Responsive Design'],
            },
            {
                'title': 'Adobe India Hackathon',
                'description': 'Completed the online MCQ assessment challenge to demonstrate coding and problem-solving skills.',
                'tags': ['Hackathon', 'Problem Solving', 'Online Assessment'],
            },
        ],
        'experience': [
            {
                'role': 'B.E. Computer Science & Engineering',
                'company': 'Gokaraju Lailavathi Engineering College, Osmania University',
                'period': '2023 - 2027',
                'description': 'Pursuing a technical degree while building web applications, data products, and cloud skills.',
            },
            {
                'role': 'Full-stack Developer',
                'company': 'Personal Projects',
                'period': '2024 - Present',
                'description': 'Creating interactive, user-focused applications with a strong emphasis on design and data.',
            },
        ],
        'certificates': [
            {
                'title': 'Participation Certificate',
                'description': 'Issued for successful participation in the technical event, showcasing active engagement and skill development.',
                'date': '2025',
                'file': 'portfolioapp/certificates/participation-cert-ebc3a9ee.pdf',
            },
            {
                'title': 'Google Cloud Compute Basics',
                'description': 'Completed foundational Google Cloud training covering compute services, VMs, and cloud architecture basics.',
                'date': '2025',
            },
            {
                'title': 'Google Arcade Certificate',
                'description': 'Completed Google Arcade technical challenge, demonstrating problem-solving and product development skills.',
                'date': '2025',
            },
            {
                'title': 'Deloitte Australia Data Analytics Job Simulation',
                'description': 'Completed practical analytics tasks focused on data visualization and business insights.',
                'date': 'Apr 2026',
            },
        ],
        'resume_file': 'portfolioapp/resume/Umadevi_Veepi_CV.pdf',
        'links': [
            {
                'label': 'Email',
                'url': 'mailto:veepiumadevi@gmail.com',
            },
            {
                'label': 'LinkedIn',
                'url': 'https://www.linkedin.com/in/umadevi-veepi-150436307',
            },
        ],
    }
    return render(request, 'portfolioapp/index.html', context)
