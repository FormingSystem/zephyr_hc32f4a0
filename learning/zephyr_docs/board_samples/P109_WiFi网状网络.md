---
id: learning.zephyr-docs.board-samples.page-109
title: WiFi网状网络
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/wifi_mesh/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wifi-mesh"></a>

# 第109章\_Wi-Fi 网状网络（Wi-Fi Mesh）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/wifi_mesh/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/wifi_mesh/README.rst/..)

<a id="overview"></a>

## 109.1 概述（Overview）

本示例在一组 ESP32 开发板之间建立自组织 Wi-Fi 网状网络（Self-organizing Wi-Fi mesh）。每个节点同时运行接入点和站点（Station）模式：站点接口向上连接父节点，软件接入点（SoftAP）接口接纳下游子节点。各节点自行选举根节点（Root）。只有根节点关联到配置的路由器，以连接外部网络；内部节点仅通过网状网络使用 `esp_wifi_mesh_send()` 和 `esp_wifi_mesh_recv()` 交换数据。

可通过 `mesh` 命令行界面（Shell）交互操作网状网络。收到的网状网络消息会即时记入日志。

本示例不承载 IP：所有节点都不在网状网络上运行网络协议栈，即使根节点连接路由器的链路也不运行。它只通过 `esp_wifi_mesh_send()`／`esp_wifi_mesh_recv()` 在节点间传递由应用自行解释的负载，适合在网状网络上自定义轻量协议、无需套接字（Sockets）、动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）或互联网访问的应用，例如向根节点汇集传感器读数，或向各节点下发命令。

如果节点需要访问外部网络，或在网状网络上运行标准 IP 功能，如套接字、DHCP、多播 DNS（mDNS），请改用 [Wi-Fi 网状网络 IP 通信（Wi-Fi Mesh IP）](P110_WiFi网状网络IP通信.md#wifi-mesh-ip)示例。在该示例中，根节点通过网络地址转换（Network Address Translation，NAT）把子节点流量转发到路由器，使各节点经根节点访问互联网，但需要遵守该示例列出的 IP-over-mesh 限制。

> 译注——mDNS 限制：本段原文将 mDNS 列为转用 IP 示例的动机，但 IP 示例的限制明确说明多播和 mDNS 无法穿过网状传输。因此转用 IP 示例可获得其支持的 IPv4 单播路径，不能据此认为 mDNS 已可用。前文“连接外部网络”也只描述根节点与路由器的关联，本例并未建立 IP 上行。

<a id="shell-commands"></a>

### 109.1.1 Shell 命令（Shell commands）

| 命令 | 说明 |
| --- | --- |
| `mesh status` | 显示本节点的层级、角色，即根节点或普通节点、路由表大小，以及 toDS 可达性。 |
| `mesh send <text>` | 通过网状网络发送文本消息。非根节点向根节点发送，根节点则向其路由表中的每个节点发送。 |

> 译注——命令所在终端：这些 mesh 命令在设备的 Zephyr Shell 中执行，主机的 UCRT64／Linux Shell 只负责构建、烧录和打开串口。send 接受一个文本参数，带空格的消息应作为一个带引号的参数输入；源码连同字符串结尾的 NUL 一起发送。
| `mesh table` | 转储路由表，即本节点可以路由到的节点地址。 |
| `mesh autotx <on\|off>` | 开关周期性后台发送功能；它每隔几秒发送一次 `hello seq=N`，默认关闭。 |

> 译注——消息与显示：当前后台发送周期为 5 秒且默认关闭；接收缓冲区为 128 字节，并强制补 NUL 后按字符串打印，长消息或内含零字节的二进制内容可能不能完整显示。原始网状 API 可传输应用负载，但此演示的日志不是任意二进制数据的无损导出。

<a id="requirements"></a>

## 109.2 硬件与配置要求（Requirements）

- 至少两块受支持的 ESP32 开发板，可采用 esp32、esp32s2、esp32s3、esp32c3、esp32c5 或 esp32c6。ESP32-C2 和 ESP32-H2 不提供网状网络库。

- 一台 2.4 GHz 路由器。本示例采用的自组织模式根据路由器可达性选举根节点，因此即使不使用外部网络，也需要路由器才能形成网状网络。

<a id="building-and-running"></a>

## 109.3 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块、工具链和目标板。网络示例须按本文准备对端、信道与路由器；加密示例须先满足引导程序前提。设备 Shell 命令与主机命令分别执行，日志仅为原文预期输出。本次未构建、烧录、配网、改写密钥或eFuse。

```text
west build -b esp32c6_devkitc/esp32c6/hpcore samples/boards/espressif/wifi_mesh
west flash
```

在 `src/main.c` 中，通过运行时调用 `esp_wifi_mesh_set_config()` 配置网状网络信道和路由器凭据，见 `esp_wifi_mesh.h`。默认路由器凭据是 `myssid`／`mypassword` 占位值，必须改为实际路由器的信息；保留占位值的节点找不到该网络，会持续搜索父节点。信道应与路由器一致。将同一镜像烧录到每块开发板。

> 译注——信道含义：当前两个 Mesh 示例都把 channel 初始化为 0，头文件规定 0 表示扫描选择，驱动也启用信道切换；1～13 才是固定信道。原文要求匹配路由器，不能误解成 0 是实际无线信道编号。

> 译注——配置时机：凭据和 mesh_id 在应用源码中的结构体赋值，在启动网状网络前调用 esp_wifi_mesh_set_config()；这表示运行时 API，并非现有 Shell 已支持交互录入凭据。按此示例修改后仍需重新构建。相同网状网络的节点应使用相同 mesh_id 和 mesh_password；根／子角色不同的台架配置则需要各自构建相应镜像。

<a id="node-role"></a>

### 109.3.1 节点角色（Node role）

`CONFIG_WIFI_ESP32_MESH_ROLE` 选择项决定节点如何加入树状拓扑：

- `CONFIG_WIFI_ESP32_MESH_ROLE_AUTO`，默认值：自组织模式。节点扫描后，如果可达路由器，就参与投票成为根节点并连接路由器；否则作为子节点加入通信范围内的网状网络节点。由于选举由路由器可达性驱动，因此需要路由器。

- `CONFIG_WIFI_ESP32_MESH_FORCE_ROOT`：把本节点固定为根节点。它不参与选举，始终位于树顶。配置了路由器时，它仍会关联路由器并维持上行链路；只有在无路由器配置下才停止父节点搜索，否则会不断扫描并不存在的父节点。

- `CONFIG_WIFI_ESP32_MESH_FORCE_CHILD`：本节点永不成为根节点，只作为子节点接入。

每种角色都需要路由器：子节点通过自组织父节点搜索接入，该过程依赖根节点与路由器的关联。完全不带路由器的网状网络需要为每个子节点显式指定父节点，而本示例未实现这一点。

在自动角色下，根节点选举取决于路由器可达性，因此都处于路由器覆盖范围内的开发板会各自成为根节点；只有超出路由器范围的节点才作为子节点加入网状网络。在所有开发板都靠近路由器的台架测试中，应为预期子节点启用 `CONFIG_WIFI_ESP32_MESH_FORCE_CHILD=y`，让它们连接到选出的根节点，而非各自成为根节点。

若要固定台架拓扑，将一块板配置为 `CONFIG_WIFI_ESP32_MESH_FORCE_ROOT=y`，其余板配置为 `CONFIG_WIFI_ESP32_MESH_FORCE_CHILD=y`。固定根节点位于第 1 层，子节点接在其下方。

<a id="sample-output"></a>

## 109.4 示例输出（Sample Output）

```text
<inf> wifi_mesh: Wi-Fi mesh starting (router SSID "myssid"), use the "mesh" shell commands
<inf> wifi_mesh: mesh started, layer -1
<inf> wifi_mesh: parent connected, layer 1 (root)
<inf> wifi_mesh: child connected
<inf> wifi_mesh: routing table size 1

uart:~$ mesh status
layer:         1
role:          root
routing table: 1 node(s)
toDS:          unreachable
autotx:        off
uart:~$ mesh send hello-mesh
sent 11 bytes over mesh
uart:~$ mesh table
routing table: 1 node(s)
 0: aa:bb:cc:dd:ee:ff

<inf> wifi_mesh: rx 11 bytes: hello-mesh
```

> 译注——源码入口：[src/main.c](../../../samples/boards/espressif/wifi_mesh/src/main.c)；[src/mesh_shell.c](../../../samples/boards/espressif/wifi_mesh/src/mesh_shell.c)；[prj.conf](../../../samples/boards/espressif/wifi_mesh/prj.conf)；[include/zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](../../../include/zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h)；[drivers/wifi/esp32/src/esp_wifi_mesh.c](../../../drivers/wifi/esp32/src/esp_wifi_mesh.c)。本地源码使用相对链接；上游快照及官方补充说明的摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/boards/espressif/wifi_mesh/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/wifi_mesh/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/wifi_mesh/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或改写密钥与eFuse。

[上一章](P108_闪存加密.md) · [返回大纲](大纲.md) · [下一章](P110_WiFi网状网络IP通信.md)
