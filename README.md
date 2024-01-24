# Resume matching
Make sure you have docker, docker compose, makefile
## Start project
Build & run docker with make command
```
make api-start
``` 
## Use api for match resume
1. Move cv file and jd file to `./resume-api/volumn` (under mount path)
2. Call api for trigger job to `http://localhost/resume_matching?jd_path={jd_path}&cv_path={cv_path}`

Example
-   Case batch one document 
```
http://localhost/resume_matching?jd_path=jd/ftp-de.txt&cv_path=cv/candidate1.pdf
```
-   Case batch many document (join string with `,`)
```
http://localhost/resume_matching?jd_path=jd/ftp-de.txt,jd/ftp-de.pdf&cv_path=cv/candidate1.pdf,cv/candidate2.pdf,cv/candidate3.pdf
```
3. Json output
```
{
    'matching_result' : [{
        "jd_path": "string",
        "cv_path": "string",
        "matching_percent": float
        }]
    , 'extract_result' : [{
            "path": "string",
            "name": "string",
            "email": "string",
            "mobile_number": "string",
            "skills": [
                "string"
            ],
            "college_name": "string",
            "degree": "string",
            "designation": "string",
            "experience": int,
            "company_names": "string",
            "no_of_pages": int,
            "total_experience": int
        }]
}
```
## Stop project
stop docker with make command
```
make api-stop
```
## To improve
- Add word set for skill extract (python lib : pyresparser.ResumeParser)
- Add parallel processing

## Reference
- [Smart_Resume_Analyser_App](https://github.com/Spidy20/Smart_Resume_Analyser_App/tree/master)
- [resume-scanner](https://randerson112358.medium.com/resume-scanner-2c30f5baf92c)
- [matching-cv-to-job-description-using-python](https://www.kaggle.com/code/nezarabdilahprakasa/matching-cv-to-job-description-using-python/notebook)