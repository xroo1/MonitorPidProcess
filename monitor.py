import time, os,sys, psutil


def banner(c1,c2):
    banner = f'''
        {c1}
            ▄▄▄              ▪
            ▀▄ █·▪     ▪    ▄██
            ▐▀▀▄  ▄█▀▄  ▄█▀▄ ▐█·
            ▐█•█▌▐█▌.▐▌▐█▌.▐▌▐█▌
            .▀  ▀ ▀█▄▀▪ ▀█▄▀▪▀▀▀

                  Monitor{c2}
    '''
    print(banner)
    pass


gr = "\033[1;32m"
rd = "\033[1;31m"
r  = "\033[0m"


def getProcessesInfo(appNames):
    processes = []
    appStatus = {appName: f'{rd}off{r}' for appName in appNames}

    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            if proc.info['name'] in appNames:
                procInfo = proc.info
                processes.append(procInfo)
                appStatus[procInfo['name']] = f'{gr}on{r}'
                pass
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        pass

    return processes, appStatus


def displayProcessesInfo(processes, appStatus):
    os.system('clear')
    print('Status dos aplicativos: ')
    for appName, status in appStatus.items():
        print(f"{appName:<25} {status}")
        pass
    print("\nDetalhes dos processos:\n")

    if processes:
        print(f"{gr}{'PID':<8} {'Name':<25} {'User':<15} {'CPU%':<10} {'Memory%':<10}{r}")
            #print("="*69)
        for proc in processes:
            print(f"{proc['pid']:<8} {proc['name']:<25} {proc['username']:<15} {proc['cpu_percent']:<10.2f} {proc['memory_percent']:<10.2f}")
            pass
        pass
    else:
        print("Nenhum dos aplicativos especificados está em execução.")
        pass
    pass


def execute():
    banner(gr,r)
    time.sleep(1)
    appNames = []
    set_elemento = int(input(f"Quantidade de elementos {gr}>>{r} "))
    for i in range(0, set_elemento):
        app = input(f"Nome do app {gr}>>{r} ")
        appNames.append(app)
        pass
    try:
        while True:
            processes, appStatus = getProcessesInfo(appNames)
            displayProcessesInfo(processes, appStatus)
            time.sleep(0.1)
    except KeyboardInterrupt:
        banner(rd,r)
        print(f"{rd} Monitoramento interropido pelo usuário.{r}")
        pass
    pass


def main():
    execute()
    pass


if __name__ == '__main__':
    main()
    pass
