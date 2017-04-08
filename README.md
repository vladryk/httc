HTTC
===========

Add test-data to database
------------

```
./manage.py loadtestdata markedskraft.Contract:100000
./manage.py loadtestdata httc.Order:100000
./manage.py loadtestdata httc.OrderSorting:100000
./manage.py loadtestdata httc.Trade:100000
./manage.py loadtestdata httc.AlgorithmSettings:100000
./manage.py loadtestdata httc.MasterSlave:100000
./manage.py loadtestdata httc.ConfirmationFile:100000
./manage.py loadtestdata httc.SMSAlert:100000
./manage.py loadtestdata markedskraft.Order:100000
./manage.py loadtestdata markedskraft.Trade:100000

```


After adding test-data can run test-functions from tasks.py
