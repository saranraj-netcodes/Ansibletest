import paramiko
from getpass import getpass
import time

def ssh_conn(host, username, password):
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(
        host,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    remote_conn = remote_conn_pre.invoke_shell()
    return (remote_conn, remote_conn_pre)

def verify_connection(ssh_conn):
    ssh_conn.send("\n\n")
    time.sleep(1)
    return my_conn.recv(20000).decode()

def disable_paging(ssh_conn, cmd="terminal length 0\n"):
    ssh_conn.send(cmd)
    time.sleep(1)
    return my_conn.recv(20000).decode()


if __name__ == "__main__":

    #Establish Connection
    password = getpass()
    my_conn, remote_conn_pre = ssh_conn(
        host= "192.168.1.201", username= "admin", password= password
    )

    #Verify Connection
    output = verify_connection(my_conn)
    print(output)

    #Disable Paging
    output = disable_paging(my_conn)
    print(output)




