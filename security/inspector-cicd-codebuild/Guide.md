Command to run:
```
terraform plan
```

Review the dry run plan, if it looks good:

```
terraform apply --auto-approve
```

After run terraform, you can add code to the codecommit repo:
```
cd ..
git clone https://git-codecommit.ap-southeast-1.amazonaws.com/v1/repos/inspector-scan-repo
cp -R inspector-cicd-codebuild/codebuild inspector-scan-repo
cd inspector-scan-repo
git add . && git commit -m '[add] code asset added' && git push
```
Note: https://git-codecommit.ap-southeast-1.amazonaws.com/v1/repos/inspector-scan-repo -> remove ap-southeast-1 to your current region if needed


Sample result:
[sample-result](./inspector-ecs-scan-sample-result.txt)
