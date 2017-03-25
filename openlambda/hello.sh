cd open-lambda
./bin/admin new -cluster my-cluster
sudo ./bin/admin workers -p 80 -cluster=my-cluster # port 80 needs root permission
./bin/admin status -cluster=my-cluster
cp -r ./quickstart/handlers/hello ./my-cluster/registry/hello
curl -X POST localhost/runLambda/hello -d '{"name": "Alice"}'
