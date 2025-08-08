def recommend_courses(keywords):
    # Simplified for demo – use APIs or web scraping for dynamic data
    catalog = {
        "python": {"title": "Python for Everybody - Coursera", "link": "https://www.coursera.org/specializations/python"},
        "data analysis": {"title": "Data Analysis with Python - freeCodeCamp", "link": "https://www.freecodecamp.org/learn/data-analysis-with-python/"},
        "machine learning": {"title": "Machine Learning - Andrew Ng (Coursera)", "link": "https://www.coursera.org/learn/machine-learning"},
        "html": {"title": "HTML Full Course - freeCodeCamp", "link": "https://www.youtube.com/watch?v=pQN-pnXPaVg"},
        "css": {"title": "CSS Full Course - freeCodeCamp", "link": "https://www.youtube.com/watch?v=ieTHC78giGQ"},
        "javascript": {"title": "JavaScript Course - freeCodeCamp", "link": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
        "ai/ml": {"title": "Intro to AI - Udacity", "link": "https://www.udacity.com/course/intro-to-artificial-intelligence--cs271"},
        "cloud": {"title": "Cloud Computing Basics - Coursera", "link": "https://www.coursera.org/learn/cloud-computing"},
    }

    results = []
    for key in keywords:
        key_lower = key.lower()
        for k in catalog:
            if k in key_lower:
                results.append(catalog[k])
    return results[:7]

def recommend_internships(keywords):
    # Static links; can use APIs (Internshala, LinkedIn) for dynamic data
    sample = {
        "python": {"title": "Python Dev Internship - Internshala", "link": "https://internshala.com/internships/python-development-internship"},
        "web development": {"title": "Web Dev Internship - LetsGrowMore", "link": "https://letsgrowmore.in/vip/"},
        "data science": {"title": "Data Science Intern - Internshala", "link": "https://internshala.com/internships/data-science-internship"},
        "ai/ml": {"title": "AI Internship - SmartInternz", "link": "https://smartinternz.com/internships"},
    }

    results = []
    for key in keywords:
        key_lower = key.lower()
        for k in sample:
            if k in key_lower:
                results.append(sample[k])
    return results[:5]
