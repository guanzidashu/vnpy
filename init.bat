::��װChocolate
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

::��װAnaconda
choco install anaconda2 --version 4.0.0 --x86 -y --ignorechecksum --params="'/AddToPath=1'"
setx PATH "%PATH%;C:\Program Files\Anaconda2\;C:\Program Files\Anaconda2\Scripts\"

::��װVC Redist
choco install vcredist2013 --x86 -y

::��װMongoDB
choco install mongodb -y

::��װGit
choco install git -y

::����vn.py
call refreshenv
cd c:\
git clone "https://github.com/vnpy/vnpy.git"

::ע��MongoDBΪϵͳ����
cd vnpy
git checkout dev

mkdir c:\data\db
mkdir c:\data\log

"C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe" --config "C:\vnpy\mongod.cfg" --install
net start MongoDB

::��װvn.py
start /wait install.bat
