 Id CommandLine
  -- -----------
   1 Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
   2 cd
   3 cd ..
   4 cd ..
   5 dir
   6 cs .\Users\
   7 cs .\Users\
   8 cd Users
   9 cd zidan\
  10 cd .aws
  11 ls
  12 chmod 400 ec21.pem
  13  ssh -i "ec21.pem" ec2-user@ec2-18-208-148-233.compute-1.amazonaws.com
  14 cd ..
  15 ls
  16 aws ec2 describe-key-pairs
  17 aws ec2 create-key-pair --key-name "ec2wf3" --query "KeyMaterial" --output text > wf3.pem
  18 aws ec2 describe-key-pairs
  19 aws ec2 describe-security-groups
  20 aws ec2 describe-vpcs
  21 aws ec2 create-security-group --group-name wf3 --description "security group pour wf3 " --vpc-id vpc-03272c7448327537f
  22 aws ec2 describe-security-groups
  23 Notepad $PROFILE
  24 if (!(Test-Path -Path $PROFILE ))...
  25 Notepad $PROFILE

  31 Notepad $PROFILE