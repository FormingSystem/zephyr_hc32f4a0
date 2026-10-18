---
id: learning.zephyr-docs.networking.page-35
title: DHCPv4客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/dhcpv4_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_DHCPv4客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/dhcpv4_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 35.1\_概览与前提（Overview and Requirements）

本应用启动 DHCPv4 客户端，从服务器获取 IPv4 地址，然后在串口控制台（Serial Console）打印地址、租约时间（Lease Time）、子网掩码（Netmask）及路由器信息。

前提见[与主机系统联网](P007_与主机系统联网.md#networking-with-host)。示例源码位于官方 [`samples/net/dhcpv4_client`](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/dhcpv4_client)。以下构建命令从 Zephyr 源码根目录执行，Linux 主机配置命令则在主机终端执行。

## 35.2\_Linux 主机与 QEMU

本节通过 QEMU 中的客户端向 Linux 主机运行的 Kea DHCPv4 服务器协商地址。QEMU 网络准备按[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)完成。

主机服务器配置文件 `/etc/kea/kea-dhcp4.conf` 的官方示例如下：

```json
{
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [ "tap0" ],
            "dhcp-socket-type": "raw"
        },

        "valid-lifetime": 7200,

        "subnet4": [
            {
                "id": 1,
                "subnet": "192.0.2.0/24",
                "pools": [ { "pool": "192.0.2.10 - 192.0.2.100" } ],
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.0.2.2"
                    },
                    {
                        "name": "domain-name-servers",
                        "data": "8.8.8.8"
                    }
                ]
            }
        ]
    }
}
```

在另一个 Linux 主机终端使用此文件启动服务器：

```sh
$ sudo kea-dhcp4 -c /etc/kea/kea-dhcp4.conf
```

> 译注：`/etc/kea/kea-dhcp4.conf` 是 Linux 系统服务配置位置，不是作者仓库路径；读者须已安装 Kea，并将上面的内容写入相应服务器配置。`tap0` 是原文测试接口，应与实际创建的接口一致。代码中的 `$` 是终端提示符，复制命令时不包含它。

在 Zephyr 开发终端构建并运行应用：

```sh
west build -b qemu_x86 samples/net/dhcpv4_client
west build -t run
```

协商成功后，官方日志如下：

```text
[00:00:00.000,000] <inf> net_dhcpv4_client_sample: Run dhcpv4 client
[00:00:00.000,000] <inf> net_dhcpv4_client_sample: Start on slip: index=1
[00:00:07.080,000] <inf> net_dhcpv4: Received: 192.0.2.10
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:    Address[1]: 192.0.2.10
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:     Subnet[1]: 255.255.255.0
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:     Router[1]: 192.0.2.2
[00:00:07.080,000] <inf> net_dhcpv4_client_sample: Lease time[1]: 7200 seconds
```

在主机执行以下命令，确认客户端已经运行并获得地址：

```sh
$ ping -I tap0 192.0.2.10
```

示例分配到 `192.0.2.10`，租约为 `7200` 秒；实际分配地址以运行日志为准。若协商未完成，应先回查 QEMU 与主机接口连接、Kea 监听接口及地址池配置。

## 35.3\_FRDM-K64F 开发板

本节使用 [FRDM-K64F 开发板](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)上的客户端，向 Linux 主机的 Kea 服务器协商地址。将开发板通过以太网线连接主机，在主机查看接口：

```sh
$ ifconfig
```

向对应主机接口添加 IP 地址与路由，原例使用 `eth1`：

```sh
$ sudo ip addr add 192.0.2.2 dev eth1
$ sudo ip route add 192.0.2.0/24 dev eth1
```

主机 `/etc/kea/kea-dhcp4.conf` 配置改为监听这个接口：

```json
{
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [ "eth1" ],
            "dhcp-socket-type": "raw"
        },

        "valid-lifetime": 7200,

        "subnet4": [
            {
                "id": 1,
                "subnet": "192.0.2.0/24",
                "pools": [ { "pool": "192.0.2.10 - 192.0.2.100" } ],
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.0.2.2"
                    },
                    {
                        "name": "domain-name-servers",
                        "data": "8.8.8.8"
                    }
                ]
            }
        ]
    }
}
```

在另一个主机终端启动服务器：

```sh
$ sudo kea-dhcp4 -c /etc/kea/kea-dhcp4.conf
```

在 Zephyr 源码根构建并烧录示例：

```sh
west build -b frdm_k64f samples/net/dhcpv4_client
west flash
```

通过串口查看协商结果。以下块首行是主机连接串口的命令，后面是原文日志：

```text
$ sudo screen /dev/ttyACM0 115200
[00:00:00.000,000] <inf> net_dhcpv4_client_sample: Run dhcpv4 client
[00:00:00.000,000] <inf> net_dhcpv4_client_sample: Start on ethernet: index=1
[00:00:07.080,000] <inf> net_dhcpv4: Received: 192.0.2.10
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:    Address[1]: 192.0.2.10
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:     Subnet[1]: 255.255.255.0
[00:00:07.080,000] <inf> net_dhcpv4_client_sample:     Router[1]: 192.0.2.2
[00:00:07.080,000] <inf> net_dhcpv4_client_sample: Lease time[1]: 7200 seconds
```

在主机验证所得地址可达：

```sh
$ ping -I eth1 192.0.2.10
```

> 译注：`eth1` 和 `/dev/ttyACM0` 都应替换为实际接口／设备节点。这里保留的是官方 FRDM-K64F 示例，不代表 HC32 板上已完成以太网适配，也不构成本轮烧录或联网测试记录。

## 35.4\_Arm FVP

原文列出 [FVP BaseR AEMv8-R](https://docs.zephyrproject.org/latest/boards/arm/fvp_baser_aemv8r/doc/index.html#fvp_baser_aemv8r) 与 [BASE RevC 2xAEM 固定虚拟平台](https://docs.zephyrproject.org/latest/boards/arm/fvp_base_revc_2xaem/doc/index.html#fvp_base_revc_2xaem)。运行在 Arm FVP 中的此示例可向 FVP 内置 DHCPv4 服务器申请地址，无需额外主机网络配置，可以直接构建运行。

以下命令以 `fvp_baser_aemv8r` 为例：

```sh
west build -b fvp_baser_aemv8r samples/net/dhcpv4_client
west build -t run
```

地址协商完成后的原始输出：

```text
uart:~$
[00:00:00.060,000] <inf> phy_mii: PHY (0) ID 16F840

[00:00:00.170,000] <inf> phy_mii: PHY (0) Link speed 10 Mb, half duplex

[00:00:00.170,000] <inf> eth_smsc91x: MAC 00:02:f7:ef:37:16
*** Booting Zephyr OS build zephyr-v3.2.0-4300-g3e6505dba29e ***
[00:00:00.170,000] <inf> net_dhcpv4_client_sample: Run dhcpv4 client
[00:00:00.180,000] <inf> net_dhcpv4_client_sample: Start on ethernet@9a000000: index=1
[00:00:07.180,000] <inf> net_dhcpv4: Received: 172.20.51.1
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:    Address[1]: 172.20.51.1
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:     Subnet[1]: 255.255.255.0
[00:00:07.180,000] <inf> net_dhcpv4_client_sample:     Router[1]: 172.20.51.254
[00:00:07.180,000] <inf> net_dhcpv4_client_sample: Lease time[1]: 86400 seconds
```

日志中的 Zephyr 版本、MAC、PHY 信息及租约是官方示例输出，不表示当前源码一定产生相同内容。

## 35.5\_相关接口

- [DHCPv4 API](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html)。
- [网络管理（Network Management）API](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html)。


<a id="dhcpv4-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="running-dhcpv4-client-in-linux-host"></a>
<a id="frdm-k64f"></a>
<a id="arm-fvp"></a>
<a id="see-also"></a>

[上一章](P034_SNTP时间同步库.md) · [返回大纲](大纲.md) · [下一章](P036_DHCPv6前缀委派示例.md)
