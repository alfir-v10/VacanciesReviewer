# VacanciesReviewer

Use [HeadHunterDatabaseDescription](https://github.com/alfir-v10/VacanciesReviewer/blob/master/HeadHunterDatabaseDescription.py) to create a database using PostgreSQL to store information about vacancies

Use [HeadHunterVacancyDescription](https://github.com/alfir-v10/VacanciesReviewer/blob/master/HeadHunterVacancyDescription.py) to create a class object that provides access to attributes containing information about the vacancy.

After creating the database, you can run a [HeadHunterCrawler](https://github.com/alfir-v10/VacanciesReviewer/blob/master/HeadHunterCrawler.py) that will add vacancies to the database.
HeadHunter Crawler uses pagination by time. You can change the time interval as you like, however, for correct operation, it is worth considering the fact that the HeadHunter API gives out no more than 2000 vacancies. The smaller the time interval, the less likely it is to go beyond this limit.
