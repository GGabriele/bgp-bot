docker exec -i helpers_ceos1_1 /bin/bash -c 'FastCli -p 15 -c "enable
configure
ip routing
management api http-commands
protocol https
no shutdown
username test secret test
int et1
no switchport
ip add 192.168.1.1/24
no shut
int lo0
ip add 100.100.100.1/24
copy run start"'
docker exec -i helpers_ceos1_1 /bin/bash -c 'chmod -R 0777 /mnt/flash'
docker exec -i helpers_ceos2_1 /bin/bash -c "FastCli -p 15 -c 'enable
configure
ip routing
management api http-commands
protocol https
no shutdown
username test secret test
int et1
no switchport
ip add 192.168.1.2/24
no shut
int lo0
ip add 200.200.200.1/24
copy run start'"
docker exec -i helpers_ceos2_1 /bin/bash -c 'chmod -R 0777 /mnt/flash'
