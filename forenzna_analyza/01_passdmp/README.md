1. ```file``` - I analysed the ```pass.dmp``` file. I found out that is is ```Mini DuMP crash report```.

2. From the task i knew that i am looking for creadentials. Good tools for extracting credentials from dumps is pypykatz. By running ```pypykatz lsa minidump pass.dmp```

3. In the output of the credentials dump i found password: ```redacted``` which was flag too
