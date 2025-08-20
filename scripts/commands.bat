
@REM הרצת קונטינר mongodb
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest



@REM בניית Img ודחיפה docker hub
docker build -t itamar12/mongodb-crud-server:latest .
docker push itamar12/mongodb-crud-server:latest


@REM מחיקת תוכן הפרוייקט
oc delete all --all
oc delete pvc --all



בניית פוד עם servis וpvc
 oc apply -f infrastructure/k8s/pvc.yaml
 oc apply -f infrastructure/k8s/deployment_mongo.yaml
 oc apply -f infrastructure/k8s/service_mongo.yaml


oc apply -f infrastructure/k8s/deployment_fastapi.yaml
oc apply -f infrastructure/k8s/service_fastapi.yaml
oc apply -f infrastructure/k8s/route.yaml 



@REM update
https://fastapi-route-ya0534516378-dev.apps.rm1.0a51.p1.openshiftapps.com/update/?id=8&field=first_name&value=kkk

@REM insert
https://fastapi-route-ya0534516378-dev.apps.rm1.0a51.p1.openshiftapps.com/insert/?id=8&first_name=Itamar&last_name=Levi&phone_number=0501234567&rank=Private

@REM get
https://fastapi-route-ya0534516378-dev.apps.rm1.0a51.p1.openshiftapps.com/data


@REM delete
https://fastapi-route-ya0534516378-dev.apps.rm1.0a51.p1.openshiftapps.com/delete/?id=9