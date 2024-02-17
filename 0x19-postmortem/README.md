# Learning to write a postmoterm report.
you will find below a copy of the said report.
please find original on: [medium](https://medium.com/@legennd48/website-x-outage-postmortem-january-8-2024-388b42da7bb8)

Website Outage Postmortem (January 8, 2024)
This report details an outage affecting our website on January 8, 2024, from 6:00 AM to 6:46 AM WAT. During this time, users were unable to access our services. We take full responsibility for this downtime and apologize for any inconvenience caused.
Issue Summary:
The outage resulted in all website requests being blocked due to a disabled configuration server file. This issue stemmed from a bug in our automation scripts that pushed an incomplete configuration update.
Timeline:
•	5:45 AM WAT: Configuration changes were deployed to live servers without proper testing.
•	6:00 AM WAT: Website becomes inaccessible.
•	6:05 AM WAT: Engineering team receives alerts and begins investigating.
•	6:15 AM WAT: Team identifies a typo in the automation script causing the configuration issue.
•	6:20 AM WAT: Root cause confirmed as a script-related error.
•	6:37 AM WAT: Patch fix deployed to correct the script.
•	6:42 AM WAT: Server restart initiated.
•	6:46 AM WAT: Website comes back online.
Root Cause And Resolution:
The root cause of the outage was a typo in the automation script that deployed the configuration update. This typo caused the server to ignore a critical configuration file, leading to the access block.
Corrective Actions:
•	Immediate: A patch was applied to fix the script error.
•	Ongoing:
o	Implement a multi-person review process for all automation scripts before deployment.
o	Enhance testing procedures to catch configuration issues before reaching production.
o	Review and strengthen script development practices to minimize typos and errors.
Corrective and Preventative Measures:
•	Enforce stricter code review and testing procedures for automation scripts.
•	Integrate automated unit tests for scripts to guarantee proper functionality.
•	Implement a staged deployment process with rollbacks in case of issues.
•	Invest in automated monitoring and alerting tools to detect similar problems faster.
This incident highlights the importance of robust testing, code review, and automation script development practices. We are committed to implementing these corrective and preventative measures to ensure similar incidents are avoided in the future.

