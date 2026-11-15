---
id: learning.zephyr-docs.networking.page-9
title: QEMU联网概览
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_QEMU联网概览

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

本页说明Linux主机与QEMU虚拟机中Zephyr应用之间的虚拟网络，例如 `qemu_x86`、`qemu_cortex_m3`。部分虚拟ARM开发板如 `qemu_cortex_a53` 只有一个UART，宜使用 [QEMU以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)。

示例在QEMU中运行 [高级回显服务器](P047_高级回显服务器示例.md#sockets-echo-server)。QEMU通过串口连接Linux主机，利用串行线路网际协议（Serial Line Internet Protocol，SLIP）沿一系列虚拟连接传输数据。

## 9.1\_前置条件

在Linux主机找到 [net-tools](https://github.com/zephyrproject-rtos/net-tools)，标准工作区位于 `tools/net-tools`，也可独立安装。原例在Debian／Ubuntu主机终端执行：

```sh
sudo apt install -y socat libpcap-dev
git clone https://github.com/zephyrproject-rtos/net-tools
cd net-tools
make
```

**原文注意（Note）**：若出现 `AX_CHECK_COMPILE_FLAG` 错误，在Debian／Ubuntu安装 `autoconf-archive` 包。

## 9.2\_基本连接流程

至少需要四个终端：终端1是已初始化Zephyr环境的开发终端；终端2、3、4均进入net-tools目录（`cd net-tools`）。

### 9.2.1\_创建辅助套接字

启动网络仿真前，先在终端2创建Unix套接字（Unix Socket）：

```sh
./loop-socat.sh
```

### 9.2.2\_启动TAP路由守护进程

在终端3执行：

```sh
sudo ./loop-slip-tap.sh
```

需要DNS的应用，此时可能还需重启主机DNS服务器，见后面的互联网访问配置。

### 9.2.3\_启动QEMU应用

在终端1的Zephyr源码根构建并启动回显服务器：

```sh
west build -b qemu_x86 samples/net/sockets/echo_server
west build -t run
```

若QEMU报错涉及 `unix:/tmp/slip.sock`，说明遗漏了创建辅助套接字步骤。`/tmp/slip.sock` 是官方工具的Linux临时套接字位置，不是仓库目录。

### 9.2.4\_运行主机应用

在终端4通过工具与QEMU应用通信，先测试ping：

```sh
ping 192.0.2.1
ping6 2001:db8::1
```

可用netcat（`nc`）通过UDP连接。下面代码块包含命令和预期回显 `foobar`：

```sh
echo foobar | nc -6 -u 2001:db8::1 4242
foobar
```

```sh
echo foobar | nc -u 192.0.2.1 4242
foobar
```

若回显服务器启用了TCP，即 `CONFIG_NET_TCP=y`，当前示例默认已启用，可执行：

```sh
echo foobar | nc -6 -q2 2001:db8::1 4242
foobar
```

**原文注意（Note）**：按 `Ctrl+C` 退出。也可用 `telnet` 实现上述连接。

### 9.2.5\_停止辅助进程

QEMU网络测试结束后，应停止初始步骤启动的守护进程和辅助程序，避免本地接口地址冲突等网络／路由问题。例如，切换到真实硬件测试，或让主机笔记本恢复日常Wi-Fi使用前应停止它们。

分别在 `loop-slip-tap.sh`、`loop-socat.sh` 所在终端按 `Ctrl+C`。在QEMU中按 `Ctrl+A`，再按 `x` 退出。

## 9.3\_经主机NAT访问互联网

Zephyr应用访问互联网可能还需额外主机设置。开发板连接到开发主机时，QEMU和真实硬件通常都需要类似设置；连接专用路由器时则通常无需这一步。

IPv4需要通过DHCP或手动设置网关。启用 [`CONFIG_NET_CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SETTINGS)、使用原文所称“Settings”配置设施的应用，应把 [`CONFIG_NET_CONFIG_MY_IPV4_GW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_MY_IPV4_GW) 设为网关IP；其他应用在运行时调用 [`net_if_ipv4_set_gw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0826491553b11c764277cde76490eb02)。例如 `CONFIG_NET_CONFIG_MY_IPV4_GW="192.0.2.2"`。

自定义QEMU应用需要为其源地址设置网络地址转换／地址伪装（NAT / Masquerading）。假定Zephyr地址为 `192.0.2.1`、接口为 `zeth`，原文要求在主机root终端执行：

```sh
iptables -t nat -A POSTROUTING -j MASQUERADE -s 192.0.2.1/24
iptables -I FORWARD 1 -i zeth -j ACCEPT
iptables -I FORWARD 1 -o zeth -m state --state RELATED,ESTABLISHED -j ACCEPT
```

还需启用IPv4转发，并检查其他iptables规则是否干扰地址伪装。root终端执行：

```sh
sysctl -w net.ipv4.ip_forward=1
```

一些应用需要DNS服务器。多个Zephyr示例默认假设主机 `192.0.2.2` 提供DNS；现代Linux发行版通常至少运行DNS代理。新建TAP后可能要重启主机DNS，使它服务新接口。例如Debian系系统：

```sh
service dnsmasq restart
```

也可以改用网络中的DNS服务器，例如公共服务器 `8.8.8.8`，通过 [`CONFIG_DNS_SERVER1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_SERVER1) 设置。

译注：原例的网络地址、接口名和DNS服务名须对应读者实际拓扑。此处Settings指网络配置选项的设施，不应仅凭名称当作持久化Settings子系统的全部用法；本轮只翻译原文，未改变任何主机路由、防火墙或DNS。

## 9.4\_两个QEMU虚拟机互联

与VM到主机的流程不同，VM到VM的连接设置是自动的。对于支持此模式的 `echo_server`、`echo_client` 等示例，准备两个已初始化Zephyr环境的开发终端。

终端1原命令：

```sh
west build -b qemu_x86 -o server samples/net/sockets/echo_server
```

这会启动服务器QEMU，等待客户端QEMU连接。终端2原命令：

```sh
west build -b qemu_x86 -o client samples/net/sockets/echo_client
```

第二个QEMU启动后，应能在两端看到数据收发日志。

> 译注：此处 `-o server`／`-o client` 是将参数传给底层构建工具，并非指定输出目录。当前west源码区分 `-o` 构建工具参数、`-t` 构建目标和 `-d` 构建目录。若从同一源码根分别构建两个应用，应使用不同构建目录，避免复用同一CMake缓存；明确分目录与server／client目标的范例见[IEEE 802.15.4互联](P012_QEMU与IEEE802154联网.md)。相应目标是否可用仍由所选网络配置决定。

## 9.5\_同一示例运行多个独立实例

若要运行多个相同示例、但它们不需彼此通信，可使用 `QEMU_INSTANCE` 参数。按所需实例数量手动启动 `socat` 和 `tunslip6`，替代 `loop-xxx.sh` 脚本。原例以 `MAIN`、`OTHER` 标识两个实例。

终端1：

```sh
socat PTY,link=/tmp/slip.devMAIN UNIX-LISTEN:/tmp/slip.sockMAIN &
sudo $ZEPHYR_BASE/../tools/net-tools/tunslip6 -t tapMAIN -T -s /tmp/slip.devMAIN 2001:db8::1/64 &
# Now run Zephyr
make -Cbuild run QEMU_INSTANCE=MAIN
```

终端2：

```sh
socat PTY,link=/tmp/slip.devOTHER UNIX-LISTEN:/tmp/slip.sockOTHER &
sudo $ZEPHYR_BASE/../tools/net-tools/tunslip6 -t tapOTHER -T -s /tmp/slip.devOTHER 2001:db8::1/64 &
make -Cbuild run QEMU_INSTANCE=OTHER
```

代码注释译文：现在运行Zephyr。

> 译注：原例中的 `make -Cbuild` 假定已存在使用Unix Makefiles生成器的 `build` 目录。当前QEMU启动脚本会让Make的 `QEMU_INSTANCE` 展开保留到运行时；不能把此Make命令直接用于Ninja构建目录。`$ZEPHYR_BASE` 由当前Zephyr开发环境提供，`../tools/net-tools` 是官方工作区相对布局；独立安装net-tools时按实际位置调整，不需要采用作者电脑的盘符路径。


> 源码跟踪译注：west 参数读取见 [`build.py`](../../../scripts/west_commands/build.py)，QEMU 启动与实例参数见 [`qemu.cmake`](../../../cmake/emu/qemu.cmake)。本轮官方串行网络目标定义另见[官方 net_serial.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/emu/qemu/net_serial.cmake)；读取文件的摘要见[来源记录](../SOURCES.md)。


<a id="networking-with-qemu"></a>
<a id="id1"></a>
<a id="contents"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="id12"></a>
<a id="id13"></a>
<a id="id14"></a>
<a id="id15"></a>
<a id="id16"></a>
<a id="id17"></a>
<a id="prerequisites"></a>
<a id="basic-setup"></a>
<a id="step-1-create-helper-socket"></a>
<a id="step-2-start-tap-device-routing-daemon"></a>
<a id="step-3-start-app-in-qemu"></a>
<a id="step-4-run-apps-on-host"></a>
<a id="step-5-stop-supporting-daemons"></a>
<a id="setting-up-zephyr-and-nat-masquerading-on-host-to-access-internet"></a>
<a id="networking-internet"></a>
<a id="network-connection-between-two-qemu-vms"></a>
<a id="terminal-1"></a>
<a id="terminal-2"></a>
<a id="running-multiple-qemu-vms-of-the-same-sample"></a>
<a id="id2"></a>
<a id="id3"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：native_sim联网](P008_native_sim联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：QEMU以太网联网](P010_QEMU以太网联网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P008_native_sim联网.md) · [返回大纲](大纲.md) · [下一章](P010_QEMU以太网联网.md)

</details>

<!-- reading-navigation:end -->
