---
id: learning.zephyr-docs.networking.page-76
title: FTP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ftp_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_FTP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ftp_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 76.1 概览（Overview）

本示例使用文件传输协议（File Transfer Protocol，FTP）客户端库，与主机上运行的 FTP 服务器交互。命令由 Zephyr 的 FTP Shell 模块提供。可[浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ftp_client/README.rst/..)。

## 76.2 运行要求（Requirements）

需要 Linux 主机，并按照[QEMU 以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)、[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)或[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备网络。

## 76.3 构建与启动（Building and Running）

在 Zephyr 源码根目录构建，替换实际开发板参数：

```shell
west build -b <board_to_use> samples/net/ftp_client
```

示例需要正在运行的 FTP 服务器。例如可使用 Python 的[pyftpdlib](https://github.com/giampaolo/pyftpdlib)模块。在 Linux 主机选定的可写工作目录中执行：

```shell
pip install pyftpdlib
mkdir file_root
echo "some test data" > file_root/test_file.txt
python3 -m pyftpdlib -p 2121 --write --directory=file_root
```

这些命令安装 Python 包，创建服务器对外暴露的根目录 `file_root`，并创建测试文件 `test_file.txt`。`--write` 以可写模式启动服务器，允许创建、删除及覆盖文件和目录。原文提醒：若将根目录换成其他位置，应注意该目录会暴露给这些操作。

> 译注：`pip` 与 `python3` 应对应同一 Python 环境，否则可能安装后找不到模块。`file_root` 是上述命令创建的测试目录，不是 Zephyr 或本仓库预先提供的目录；本轮没有启动服务器或开放目录。

另开终端，在已取得的 `net-tools` 目录启动 `net-setup.sh`：

```shell
./net-setup.sh
```

再在 Zephyr 源码根目录构建并运行 native_sim 版本：

```shell
west build -b native_sim samples/net/ftp_client
west build -t run
```

示例打印启动信息，并提供网络 Shell 命令：

```text
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> ftp_client_sample: Starting FTP client sample
[00:00:00.110,000] <inf> ftp_client_sample: Network connectivity established.
[00:00:00.110,000] <inf> ftp_client_sample: You can interact with FTP server via shell.
```

## 76.4 连接和读取文件

以下均在设备／模拟器 Shell 中操作，`uart:~$` 是提示符，不是主机命令的一部分。使用 `net ftp connect` 连接服务器；原文服务器默认接受匿名用户（Anonymous User）及占位密码：

```text
uart:~$ net ftp connect anonymous null 192.0.2.2 2121
220 pyftpdlib 2.1.0 ready.
530 Log in with USER and PASS first.
331 Username ok, send password.
230 Login successful.
```

原文输出中先出现 `530`，随后用户名和密码流程完成并返回 `230 Login successful`。应结合完整登录结果判断，不能把最初一行视为整个连接已失败。`null` 是这里传入的密码字符串。

连接成功后，可操作服务器所暴露的文件系统。列出目录内容：

```text
uart:~$ net ftp ls
227 Entering passive mode (192,0,2,2,146,7).
150 File status okay. About to open data connection.
-rw-r--r--   1 user     domain users       15 Feb 20 11:16 test_file.txt
226 Transfer complete.
```

读取文件内容：

```text
uart:~$ net ftp get test_file.txt
227 Entering passive mode (192,0,2,2,222,177).
150 File status okay. About to open data connection.
some test data
226 Transfer complete.
```

> 源码核对译注：当前官方 [FTP Shell 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/ftp.c) 通过数据回调把接收内容打印到 Shell。此处 `get` 演示读取并显示，不会自动在设备文件系统中创建同名文件。原日志中的被动模式（Passive Mode）地址和端口是服务器数据连接信息。

## 76.5 创建目录、上传和删除

创建目录、切换服务器工作目录，并打印当前位置：

```text
uart:~$ net ftp mkdir test_dir
257 "/test_dir" directory created.
uart:~$ net ftp cd test_dir
250 "/test_dir" is the current directory.
uart:~$ net ftp pwd
257 "/test_dir" is the current directory.
```

`/test_dir` 是 FTP 服务器虚拟根下的路径，不是作者机器上的仓库绝对位置。在本例服务器配置下，对应测试目录中的 `file_root/test_dir`。

创建文件、读取其内容，然后删除：

```text
uart:~$ net ftp put new_file.txt
Input mode (max 2048 characters). End the line with \ to start a new one:
New file content\

227 Entering passive mode (192,0,2,2,131,169).
150 File status okay. About to open data connection.
226 Transfer complete.
uart:~$ net ftp get new_file.txt
227 Entering passive mode (192,0,2,2,140,157).
150 File status okay. About to open data connection.
New file content
226 Transfer complete.
uart:~$ net ftp rm new_file.txt
250 File removed.
```

> 源码核对译注：不带内容参数的 `put` 进入交互输入。原提示的最多 2048 字符对应当前 Shell 缓冲区；行末单个反斜杠表示继续下一行，并转换为换行符；不续行时结束输入。原例文件内容及传输回复保留，不是本轮上传结果。

断开连接：

```text
uart:~$ net ftp disconnect
221 Goodbye.
```

## 76.6 完整命令帮助

使用 `--help` 查看支持的命令，原文输出如下：

```text
uart:~$ net ftp --help
ftp - FTP client commands
Subcommands:
  connect     : Connect to FTP server.
                Usage: connect <username> <password> <hostname> [<port> <sec_tag>]
  disconnect  : Disconnect from FTP server.
                Usage: disconnect
  status      : Print connection status.
                Usage: status
  pwd         : Print working directory.
                Usage: pwd
  ls          : List information about folder or file.
                Usage: ls [<options> <path>]
  cd          : Change working directory.
                Usage: cd <path>
  mkdir       : Create directory.
                Usage: mkdir <dir_name>
  rmdir       : Delete directory.
                Usage: rmdir <dir_name>
  rename      : Rename a file.
                Usage: rename <old_name> <new_name>
  rm          : Delete a file.
                Usage: rm <file_name>
  get         : Read file content.
                Usage: get <file_name>
  put         : Write to a file.
                Usage: put <file_name> [<data>]
  append      : Append a file.
                Usage: append <file_name> <data>
  mode        : Select transfer type.
                Usage: mode <ascii/binary>
```

这些命令分别用于连接／断开、连接状态、当前目录、列表、切换目录、创建／删除目录、重命名、删除文件、读／写／追加以及选择 ASCII／二进制传输类型（Transfer Type）。

> 源码核对译注：当前 Shell 的 `put`、`append` 均仅接收文件名，然后进入交互输入；原帮助中的 `put <file_name> [<data>]` 与 `append <file_name> <data>` 已与当前实现不一致。原帮助原样保留，实际参数应以目标固件的帮助和对应版本源码为准。

## 76.7 相关参考（See Also）

参见[FTP 客户端库 API](P080_FTP完整API参考.md)。本轮未安装依赖、构建、建立主机网络、启动服务器或进行文件创建、覆盖和删除操作。


<a id="ftp-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P075_FTP客户端库.md) · [返回大纲](大纲.md) · [下一章](P077_TFTP客户端库.md)
