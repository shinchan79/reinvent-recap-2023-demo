
1. Amazon Inspector - Amazon's managed security assessment service that can automatically scan Lambda functions for vulnerabilities. It analyzes application packages, dependencies and code to check for issues like injection flaws, data leaks etc.
2. Amazon Inspector uses the Amazon CodeGuru Detector Library which has trained models to detect security flaws in code like XSS, injection issues, log injection etc.
3. When you enable code scanning in Amazon Inspector, it will scan supported Lambda runtimes like Java, Node.js, Python, Go and provide a detailed list of findings prioritized by severity.
4. You can test scanning Lambda functions with Amazon Inspector by enabling the free trial and following the steps in the documentation. The documentation also provides more details on supported operating systems and programming languages.
5. Tools like Snyk can also integrate with your CI/CD pipelines to scan Lambda function code for vulnerabilities in dependencies.

Amazon Inspector support provides continuous, automated security vulnerability assessments for Lambda functions and layers. Amazon Inspector provides two scan types for Lambda:

- **Lambda standard scanning (default)**: Scans application dependencies within a Lambda function and its layers for package vulnerabilities.

- **Lambda code scanning**: Scans the custom application code in your functions and layers for code vulnerabilities. You can either activate Lambda standard scanning or activate Lambda standard scanning together with Lambda code scanning.

More info: 
https://docs.aws.amazon.com/lambda/latest/dg/governance-code-scanning.html

