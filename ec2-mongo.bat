IF EXIST "_PATH_TO_result.csv" (
	rm _PATH_TO_result.csv
)
scp -i _PATH_TO_KEY.pem ec2-user@_INSERT_INSTANCE_DNS_HERE_:/home/ec2-user/projet/result.csv C:/Dev/pbd
mongoimport -d pbd_cty -c result --drop --type csv --file _PATH_TO_result.csv --headerline
rm _PATH_TO_result.csv