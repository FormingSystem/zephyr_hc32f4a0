---
id: learning.zephyr-docs.networking.page-182
title: OCPP充电桩示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ocpp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第182章\_OCPP充电桩示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ocpp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

开放充电桩协议（Open Charge Point Protocol，OCPP）用于充电桩（Charge Point，CP，即电动汽车 EV 充电站）与中央管理系统之间的通信，后者也称充电站网络。

这个 Zephyr 示例使用 OCPP 库，通过 WebSocket 建立与中央系统（Central System，CS）服务器的连接。源码位于官方[samples/net/ocpp](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/ocpp)。

## 2. 要求（Requirements）

- Linux 主机。
- STM32 Discovery 套件（32F769IDISCOVERY），或其他具有网络接口的设备。
- [SteVe 演示服务器](https://github.com/steve-community/steve/blob/master/README.md)。
- 用于测试的局域网（Local Area Network，LAN），原文采用以太网。

## 3. 配置（Configuration）

示例通过 Kconfig 提供以下选项：

| 配置 | 说明 |
| --- | --- |
| [`CONFIG_NET_SAMPLE_OCPP_SERVER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/Kconfig) | OCPP 中央系统服务器 IP 地址。 |
| [`CONFIG_NET_SAMPLE_OCPP_PORT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/Kconfig) | 中央系统服务器端口。 |
| [`CONFIG_NET_SAMPLE_OCPP_WS_PATH`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/Kconfig) | WebSocket URL 路径。 |
| [`CONFIG_NET_SAMPLE_SNTP_SERVER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/Kconfig) | 用于从网络获取时间的简单网络时间协议（Simple Network Time Protocol，SNTP）服务器 IP 地址。 |

> 源码对照：当前[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/prj.conf)把 OCPP 和 SNTP 服务器字段留空，读者需填入自己的开发环境信息；默认 OCPP 端口是 `8180`，SNTP 端口是 `123`。[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/Kconfig)给出的 WebSocket 默认路径为 `/steve/websocket/CentralSystemService/zephyr`。这条路径是服务器 URL 的组成部分，不是作者机器上的目录。

## 4. 可选：生成 TLS 密钥和证书

### 4.1 生成 ECDSA 私钥

使用 OpenSSL 生成椭圆曲线数字签名算法（Elliptic Curve Digital Signature Algorithm，ECDSA）私钥：

```sh
openssl ecparam -name prime256v1 -genkey -noout -out ec-priv.key
```

### 4.2 生成自签名证书

使用 OpenSSL 生成自签名证书（Self-Signed Certificate）：

```sh
openssl req -new -x509 -key ec-priv.key -days 3650 \
-subj "/CN=localhost" -outform PEM -out ec.crt
```

> 译注：这两条是主机终端命令，输出 `ec-priv.key` 和 `ec.crt` 到当前工作目录；`/CN=localhost` 是证书主题参数，不是文件系统绝对路径。`-days 3650` 是原文有效期。生成文件仅完成材料准备，不会自动把证书加入 Zephyr 固件或配置服务器 TLS。

> 源码边界：当前示例[CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/CMakeLists.txt)在启用 TLS 且不使用虚拟凭据时调用证书生成函数，但输入证书和输出 `.inc` 路径仍是注释占位；[certificate.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/credentials/certificate.h)也要求填入实际 PEM／DER 证书，默认内容并非有效证书。它把对端主机名设为 `localhost`；实际连接时还需让证书与验证名称匹配。故本页的两条 OpenSSL 命令不是完整 TLS 接入流程，本次没有把它标记为构建或握手验证通过。

## 5. 构建与运行

在已具备 Zephyr 环境及目标板依赖的主机上，从读者自己的 Zephyr 源码根目录构建：

```sh
west build -b <board to use> samples/net/ocpp
```

`<board to use>` 应替换为目标开发板。原文说明示例曾在以下开发板上构建、测试，并给出：

```sh
west build -b stm32f769i_disco
west flash
```

> 译注：第二段没有写应用路径，只有在适当的应用当前目录或既有构建上下文中才有相应含义。如果仍从 Zephyr 源码根目录执行，应使用第一段的形式，指定 `stm32f769i_disco` 和 [`samples/net/ocpp`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp)。本次保留官方片段，但没有把原文的历史测试状态改称当前版本或本机已通过。

## 6. 示例输出

以下为官方原始输出，完整保留版本串、IP 地址、时间和两个连接器的日志：

```console
*** Booting Zephyr OS build v3.6.0-rc1-37-g8c035d8f24cf ***
OCPP sample stm32f769i_disco
[00:00:02.642,000] <inf> net_dhcpv4: Received: 192.168.1.101
[00:00:02.642,000] <inf> main: net mgr cb
[00:00:02.642,000] <inf> main: Your address: 192.168.1.101
[00:00:02.642,000] <inf> main: Lease time: 86400 seconds
[00:00:02.642,000] <inf> main: Subnet: 255.255.255.0
[00:00:02.643,000] <inf> main: Router: 192.168.1.1
[00:00:07.011,000] <inf> main: cs server 122.165.245.213 8180
[00:00:07.011,000] <inf> main: IPv4 Address 122.165.245.213
[00:00:07.024,000] <inf> main: sntp succ since Epoch: 1707890823
[00:00:07.024,000] <inf> ocpp: upstream init
[00:00:07.025,000] <inf> ocpp: ocpp init success
[00:00:17.066,000] <inf> main: ocpp auth 0> idcon 1 status 1
[00:00:17.101,000] <inf> main: ocpp auth 0> idcon 2 status 1
[00:00:17.197,000] <inf> main: ocpp start charging connector id 1
[00:00:17.255,000] <inf> main: ocpp start charging connector id 2
[00:01:07.064,000] <inf> main: ocpp stop charging connector id 1
[00:01:08.063,000] <inf> main: ocpp stop charging connector id 2
```

日志先显示 DHCP 地址与路由、CS 地址、SNTP 同步，然后初始化 OCPP，授权连接器 `1` 和 `2`，开始并停止模拟充电。日志里的服务器地址是原始运行记录，应使用自己的开发 CS，不把历史地址当作可调用的公共服务。

> 源码对照：当前[main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)为两个连接器使用 `ZepId00`、`ZepId01` 作为本地请求的用户标识，开发服务器需有相应授权数据。示例检查 `OCPP_AUTH_ACCEPTED` 后才请求事务开始；计量回调递增模拟数值，事务开始／结束读数还使用随机数，因此输出表示协议演示，不是实际计量或功率输出结果。应区分服务器返回、授权状态、事务状态及真实硬件状态。

## 7. 另见（See Also）

[OCPP 库 API](P191_OCPP完整API参考.md)。

> 验证边界：本章已核对官方页面、配置、示例和 TLS 占位实现；没有生成密钥、搭建 SteVe、连接日志中的服务器、构建或烧写开发板，也没有进行实际充电测试。


<a id="ocpp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="configuration"></a>
<a id="generating-keys-and-certificate-for-tls-optional"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P181_MCP服务器入门示例.md) · [返回大纲](大纲.md) · [下一章](P183_MCP完整API参考.md)
