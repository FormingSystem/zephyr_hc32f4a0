---
id: learning.zephyr-docs.kconfig-reference.page-193
title: "`drivers/wifi`配置项参考（6/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第193章\_`drivers/wifi`配置项参考（6/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WIFI_ESP32_MESH_XON_QSIZE"></a>

## 193.1 `CONFIG_WIFI_ESP32_MESH_XON_QSIZE`

**提示（Prompt）**：网状网络接收流量控制队列大小（Mesh receive flow-control queue size）

**说明（Help）**

mesh 接收队列在对上游发送方施加流量控制（flow control）之前可保存的数据包数量。更大的队列能容忍更大的流量突发，代价是消耗更多 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT"></a>

## 193.2 `CONFIG_WIFI_ESP_AT`

**提示（Prompt）**：乐鑫（Espressif）AT 命令支持

**说明（Help）**

启用乐鑫（Espressif）AT 命令卸载型 Wi-Fi 驱动（offloaded WiFi driver）。它支持任何具有串行通信能力的平台，并与运行 [ESP-AT 固件](https://github.com/espressif/esp-at)的乐鑫芯片通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_AT_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MODEM
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_CMD_HANDLER
CONFIG_MODEM_IFACE_UART
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_OFFLOAD
```

**弱选择（Implies）**

```text
CONFIG_UART_USE_RUNTIME_CONFIGURE
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_MODEM_IFACE_UART`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_IFACE_UART)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)、[`CONFIG_UART_USE_RUNTIME_CONFIGURE`](P169_drivers_serial_配置项参考_5.md#CONFIG_UART_USE_RUNTIME_CONFIGURE)。

<a id="CONFIG_WIFI_ESP_AT_CIPDINFO_USE"></a>

## 193.3 `CONFIG_WIFI_ESP_AT_CIPDINFO_USE`

**提示（Prompt）**：使用 CIPDINFO 获取对端 IP 地址和端口（peer IP and port）

**说明（Help）**

启用 `AT+CIPDINFO`，以获取对端 IP 地址和端口（peer IP address and port）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_DNS_RESOLVER
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)。

<a id="CONFIG_WIFI_ESP_AT_DNS_USE"></a>

## 193.4 `CONFIG_WIFI_ESP_AT_DNS_USE`

**提示（Prompt）**：使用 ESP 提供的域名系统（DNS）

**说明（Help）**

使用 `AT+CIPDNS?` 命令从 ESP 芯片获取 DNS 服务器，并将该列表应用于系统 DNS 解析器（resolver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_FETCH_VERSION"></a>

## 193.5 `CONFIG_WIFI_ESP_AT_FETCH_VERSION`

**提示（Prompt）**：获取并记录 ESP-AT 固件版本（firmware version）

**说明（Help）**

获取 ESP-AT 固件版本信息，包括 AT 命令版本、软件开发工具包（SDK，ESP-IDF）、开发板和编译时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_IP_ADDRESS"></a>

## 193.6 `CONFIG_WIFI_ESP_AT_IP_ADDRESS`

**提示（Prompt）**：ESP 站点模式（Station mode）的 IP 地址

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT_IP_STATIC && CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_IP_STATIC`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_IP_STATIC)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_IP_DHCP"></a>

## 193.7 `CONFIG_WIFI_ESP_AT_IP_DHCP`

**提示（Prompt）**：动态主机配置协议（DHCP）

**说明（Help）**

使用动态主机配置协议（DHCP）获取 IP 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持 → ESP IP 地址配置

<a id="CONFIG_WIFI_ESP_AT_IP_GATEWAY"></a>

## 193.8 `CONFIG_WIFI_ESP_AT_IP_GATEWAY`

**提示（Prompt）**：网关地址（Gateway Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT_IP_STATIC && CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_IP_STATIC`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_IP_STATIC)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_IP_MASK"></a>

## 193.9 `CONFIG_WIFI_ESP_AT_IP_MASK`

**提示（Prompt）**：网络掩码（Network Mask）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT_IP_STATIC && CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_IP_STATIC`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_IP_STATIC)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_IP_STATIC"></a>

## 193.10 `CONFIG_WIFI_ESP_AT_IP_STATIC`

**提示（Prompt）**：静态（Static）

**说明（Help）**

设置静态 IP 地址（Static IP Address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持 → ESP IP 地址配置

<a id="CONFIG_WIFI_ESP_AT_MDM_RING_BUF_SIZE"></a>

## 193.11 `CONFIG_WIFI_ESP_AT_MDM_RING_BUF_SIZE`

**提示（Prompt）**：调制解调器环形缓冲区（Modem ring buffer）大小

**说明（Help）**

调制解调器 UART 接口处理程序（modem UART interface handler）使用的环形缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_MDM_RX_BUF_COUNT"></a>

## 193.12 `CONFIG_WIFI_ESP_AT_MDM_RX_BUF_COUNT`

**提示（Prompt）**：调制解调器接收缓冲区（Modem RX buffer）数量

**说明（Help）**

调制解调器命令处理程序（modem command handler）使用的预分配接收缓冲区（RX buffers）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_MDM_RX_BUF_SIZE"></a>

## 193.13 `CONFIG_WIFI_ESP_AT_MDM_RX_BUF_SIZE`

**提示（Prompt）**：调制解调器接收缓冲区（Modem RX buffer）大小

**说明（Help）**

调制解调器命令处理程序（modem command handler）使用的预分配接收缓冲区（RX buffers）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_PASSIVE_MODE"></a>

## 193.14 `CONFIG_WIFI_ESP_AT_PASSIVE_MODE`

**提示（Prompt）**：使用被动模式（passive mode）

**说明（Help）**

让 ESP 处理 TCP 窗口（TCP window），使数据能够以驱动可处理的速率传输。不启用此选项时，如果驱动无法足够快地清空设备缓冲区，就可能丢失数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_RESET_TIMEOUT"></a>

## 193.15 `CONFIG_WIFI_ESP_AT_RESET_TIMEOUT`

**提示（Prompt）**：复位超时（Reset timeout）

**说明（Help）**

发送 `AT+RST` 后等待设备就绪的时间。此时间可能随芯片组（ESP8266／ESP32）和固件版本变化。如果配置了复位引脚（reset pin），则忽略此设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
3000
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_RX_NET_PKT_ALLOC_TIMEOUT"></a>

## 193.16 `CONFIG_WIFI_ESP_AT_RX_NET_PKT_ALLOC_TIMEOUT`

**提示（Prompt）**：网络接口接收数据包分配超时（RX packet allocation timeout）

**说明（Help）**

网络接口接收 `net_pkt` 的分配超时，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_RX_STACK_SIZE"></a>

## 193.17 `CONFIG_WIFI_ESP_AT_RX_STACK_SIZE`

**提示（Prompt）**：乐鑫（Espressif）ESP Wi-Fi 驱动接收线程（RX thread）栈大小

**说明（Help）**

乐鑫（Espressif）ESP 接收线程（RX thread）使用此栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_RX_THREAD_PRIORITY"></a>

## 193.18 `CONFIG_WIFI_ESP_AT_RX_THREAD_PRIORITY`

**提示（Prompt）**：接收线程（RX thread）优先级

**说明（Help）**

用于处理接收数据（RX data）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_SCAN_MAC_ADDRESS"></a>

## 193.19 `CONFIG_WIFI_ESP_AT_SCAN_MAC_ADDRESS`

**提示（Prompt）**：扫描响应（scan response）中的 MAC 地址

**说明（Help）**

获取扫描响应（scan response）中的 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_SCAN_PASSIVE"></a>

## 193.20 `CONFIG_WIFI_ESP_AT_SCAN_PASSIVE`

**提示（Prompt）**：被动扫描（Passive scan）

**说明（Help）**

使用被动扫描（passive scanning）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_SCAN_RESULT_RSSI_ORDERED"></a>

## 193.21 `CONFIG_WIFI_ESP_AT_SCAN_RESULT_RSSI_ORDERED`

**提示（Prompt）**：基于接收信号强度指示（RSSI）的扫描结果排序

**说明（Help）**

基于接收信号强度指示（RSSI）排序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_TCP_SEND_TIMEOUT"></a>

## 193.22 `CONFIG_WIFI_ESP_AT_TCP_SEND_TIMEOUT`

**提示（Prompt）**：TCP 套接字发送超时（TCP socket send timeout）

**说明（Help）**

对于 TCP 套接字（socket），发送 `AT+CIPSEND` 后等待设备回复 `SEND OK`／`SEND FAIL` 的时间，单位为毫秒。此时间可能随网络流量状况变化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30000
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_VERSION"></a>

## 193.23 `CONFIG_WIFI_ESP_AT_VERSION`

**提示（Prompt）**：AT 命令版本（AT version）

**说明（Help）**

选择要使用的 AT 命令集（AT command set）版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_ESP_AT_VERSION_2_1
```

**可选项（Choices）**

```text
CONFIG_WIFI_ESP_AT_VERSION_1_7
CONFIG_WIFI_ESP_AT_VERSION_2_0
CONFIG_WIFI_ESP_AT_VERSION_2_1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/esp_8266/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/esp_8266/Kconfig.defconfig)。

```text
CONFIG_WIFI_ESP_AT_VERSION_1_7
```

来源：[`boards/shields/mikroe_wifi_bt_click/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/mikroe_wifi_bt_click/Kconfig.defconfig)。

```text
CONFIG_WIFI_ESP_AT_VERSION_2_0
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_ESP_AT_VERSION_2_1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION_2_1)、[`CONFIG_WIFI_ESP_AT_VERSION_1_7`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION_1_7)、[`CONFIG_WIFI_ESP_AT_VERSION_2_0`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION_2_0)。

<a id="CONFIG_WIFI_ESP_AT_VERSION_1_7"></a>

## 193.24 `CONFIG_WIFI_ESP_AT_VERSION_1_7`

**提示（Prompt）**：AT 命令版本 1.7

**说明（Help）**

使用 1.7 版 AT 命令集（AT command set）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP_AT_VERSION>
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持 → AT 命令版本（AT version）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_VERSION`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION)。

<a id="CONFIG_WIFI_ESP_AT_VERSION_2_0"></a>

## 193.25 `CONFIG_WIFI_ESP_AT_VERSION_2_0`

**提示（Prompt）**：AT 命令版本 2.0

**说明（Help）**

使用 2.0 版 AT 命令集（AT command set）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP_AT_VERSION>
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持 → AT 命令版本（AT version）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_VERSION`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION)。

<a id="CONFIG_WIFI_ESP_AT_VERSION_2_1"></a>

## 193.26 `CONFIG_WIFI_ESP_AT_VERSION_2_1`

**提示（Prompt）**：AT 命令版本 2.1

**说明（Help）**

使用 2.1 版 AT 命令集（AT command set）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP_AT_VERSION>
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持 → AT 命令版本（AT version）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT_VERSION`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT_VERSION)。

<a id="CONFIG_WIFI_ESP_AT_WORKQ_STACK_SIZE"></a>

## 193.27 `CONFIG_WIFI_ESP_AT_WORKQ_STACK_SIZE`

**提示（Prompt）**：ESP 驱动工作队列（work queue）栈大小

**说明（Help）**

工作队列（Work Queue）使用此栈，将 `net_pkt` 数据交给网络协议栈的其他部分，使接收线程能继续处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_AT_WORKQ_THREAD_PRIORITY"></a>

## 193.28 `CONFIG_WIFI_ESP_AT_WORKQ_THREAD_PRIORITY`

**提示（Prompt）**：工作队列线程（work queue thread）优先级

**说明（Help）**

用于处理驱动工作队列项（work queue items）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_AT && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/esp_at/Kconfig.esp_at:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_at/Kconfig.esp_at#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 乐鑫（Espressif）AT 命令支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED"></a>

## 193.29 `CONFIG_WIFI_ESP_HOSTED`

**提示（Prompt）**：ESP_HOSTED 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_HOSTED_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_SPI
CONFIG_WIFI_NM
CONFIG_NANOPB
CONFIG_NANOPB_ENABLE_MALLOC
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)、[`CONFIG_NANOPB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NANOPB)、[`CONFIG_NANOPB_ENABLE_MALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NANOPB_ENABLE_MALLOC)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)。

<a id="CONFIG_WIFI_ESP_HOSTED_AP_CHANNEL_DEF"></a>

## 193.30 `CONFIG_WIFI_ESP_HOSTED_AP_CHANNEL_DEF`

**提示（Prompt）**：默认接入点信道（AP channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
9
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_AP_CLIENTS_MAX"></a>

## 193.31 `CONFIG_WIFI_ESP_HOSTED_AP_CLIENTS_MAX`

**提示（Prompt）**：最大接入点客户端数（AP clients）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_DEBUG"></a>

## 193.32 `CONFIG_WIFI_ESP_HOSTED_DEBUG`

**提示（Prompt）**：额外调试消息（debugging messages）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_POLL_MS"></a>

## 193.33 `CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_POLL_MS`

**提示（Prompt）**：事件任务轮询周期（Poll Rate），单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_PRIORITY"></a>

## 193.34 `CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_PRIORITY`

**提示（Prompt）**：事件任务优先级（Task Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_STACK_SIZE"></a>

## 193.35 `CONFIG_WIFI_ESP_HOSTED_EVENT_TASK_STACK_SIZE`

**提示（Prompt）**：事件任务栈大小（Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_MCU"></a>

## 193.36 `CONFIG_WIFI_ESP_HOSTED_MCU`

**提示（Prompt）**：ESP-Hosted-MCU 驱动支持

**说明（Help）**

主机驱动（host driver），用于将运行 `esp-hosted-mcu` 协处理器固件（coprocessor firmware）的乐鑫（Espressif）SoC（例如 ESP32-C6）作为 Wi-Fi 协处理器。通过 SPI 或 SDIO，使用 `esp-hosted-mcu` 传输核心（transport core）进行通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_HOSTED_MCU_WIFI_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP_HOSTED_MCU
CONFIG_WIFI_NM
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)。

<a id="CONFIG_WIFI_ESP_HOSTED_MCU_AP_CHANNEL_DEF"></a>

## 193.37 `CONFIG_WIFI_ESP_HOSTED_MCU_AP_CHANNEL_DEF`

**提示（Prompt）**：默认接入点信道（AP channel）

**说明（Help）**

连接请求未指定信道时，软件接入点（soft-AP）启动所使用的信道（channel）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED_MCU_AP_STA_MODE && CONFIG_WIFI_ESP_HOSTED_MCU && CONFIG_WIFI
```

**默认值（Defaults）**

```text
9
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP-Hosted-MCU 驱动支持 → 软件接入点接口（Soft-AP interface）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED_MCU_AP_STA_MODE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU_AP_STA_MODE)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_MCU_AP_STA_MODE"></a>

## 193.38 `CONFIG_WIFI_ESP_HOSTED_MCU_AP_STA_MODE`

**提示（Prompt）**：软件接入点接口（Soft-AP interface）支持

**说明（Help）**

注册软件接入点（soft-AP，`sap_if`）网络接口及接入点管理操作（access point management operations）。未启用时，仅存在站点（station）接口。启用软件接入点时，协处理器仍以 AP-STA 组合模式运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED_MCU && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_STA_AP || CONFIG_WIFI_USAGE_MODE_AP
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted_mcu/Kconfig.esp_hosted_mcu#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP-Hosted-MCU 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_USAGE_MODE_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_AP)。

<a id="CONFIG_WIFI_ESP_HOSTED_RX_QUEUE_SIZE"></a>

## 193.39 `CONFIG_WIFI_ESP_HOSTED_RX_QUEUE_SIZE`

**提示（Prompt）**：接收消息队列（RX message queue）大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP_HOSTED_TX_QUEUE_SIZE"></a>

## 193.40 `CONFIG_WIFI_ESP_HOSTED_TX_QUEUE_SIZE`

**提示（Prompt）**：发送消息队列大小（TX Message Queue Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP_HOSTED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/wifi/esp_hosted/Kconfig.esp_hosted:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp_hosted/Kconfig.esp_hosted#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP_HOSTED 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESWIFI"></a>

## 193.41 `CONFIG_WIFI_ESWIFI`

**提示（Prompt）**：Inventek eS-WiFi 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_INVENTEK_ESWIFI_ENABLED || DT_HAS_INVENTEK_ESWIFI_UART_ENABLED) && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_OFFLOAD
CONFIG_NET_OFFLOAD
CONFIG_NET_SOCKETS
CONFIG_GPIO
```

**弱选择（Implies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/esp_8266/boards/disco_l475_iot1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/esp_8266/boards/disco_l475_iot1.defconfig)。

```text
n
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)。

<a id="CONFIG_WIFI_ESWIFI_BUS"></a>

## 193.42 `CONFIG_WIFI_ESWIFI_BUS`

**提示（Prompt）**：选择总线接口（BUS interface）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESWIFI && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_ESWIFI_BUS_SPI
```

**可选项（Choices）**

```text
CONFIG_WIFI_ESWIFI_BUS_SPI
CONFIG_WIFI_ESWIFI_BUS_UART
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/inventek_eswifi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/inventek_eswifi/Kconfig.defconfig)。

```text
CONFIG_WIFI_ESWIFI_BUS_SPI if CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_SPI
```

来源：[`boards/shields/inventek_eswifi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/inventek_eswifi/Kconfig.defconfig)。

```text
CONFIG_WIFI_ESWIFI_BUS_UART if CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_UART
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_ESWIFI_BUS_SPI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI_BUS_SPI)、[`CONFIG_WIFI_ESWIFI_BUS_UART`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI_BUS_UART)、[`CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_SPI)、[`CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_UART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_SPI`、`CONFIG_SHIELD_INVENTEK_ESWIFI_ARDUINO_UART`。

<a id="CONFIG_WIFI_ESWIFI_BUS_SPI"></a>

## 193.43 `CONFIG_WIFI_ESWIFI_BUS_SPI`

**提示（Prompt）**：SPI 总线接口（Bus interface）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESWIFI_BUS>
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持 → 选择总线接口（BUS interface）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESWIFI_BUS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI_BUS)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_WIFI_ESWIFI_BUS_UART"></a>

## 193.44 `CONFIG_WIFI_ESWIFI_BUS_UART`

**提示（Prompt）**：UART 总线接口（Bus interface）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESWIFI_BUS>
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持 → 选择总线接口（BUS interface）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESWIFI_BUS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI_BUS)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_WIFI_ESWIFI_MAX_DATA_SIZE"></a>

## 193.45 `CONFIG_WIFI_ESWIFI_MAX_DATA_SIZE`

**提示（Prompt）**：esWiFi 消息大小（message size）

**说明（Help）**

设置 esWiFi 消息缓冲区（message buffer）的大小。可增大此值，以处理更大的消息，例如扫描结果（scan results）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESWIFI && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1600
```

**取值范围（Ranges）**

```text
[500, 4000]
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESWIFI_SHELL"></a>

## 193.46 `CONFIG_WIFI_ESWIFI_SHELL`

**提示（Prompt）**：esWiFi 命令行（shell）

**说明（Help）**

启用 esWiFi 命令行（shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_WIFI_ESWIFI && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESWIFI_THREAD_PRIO"></a>

## 193.47 `CONFIG_WIFI_ESWIFI_THREAD_PRIO`

**提示（Prompt）**：esWiFi 线程优先级（threads priority）

**说明（Help）**

设置 esWiFi 线程的优先级（priority）。除非清楚修改的影响，否则不要更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESWIFI && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/eswifi/Kconfig.eswifi:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/eswifi/Kconfig.eswifi#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Inventek eS-WiFi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_FIXED_MAC_ADDRESS"></a>

## 193.48 `CONFIG_WIFI_FIXED_MAC_ADDRESS`

**提示（Prompt）**：Wi-Fi 固定 MAC 地址，格式为 `XX:XX:XX:XX:XX:XX`

**说明（Help）**

覆盖从一次性可编程存储器（OTP）读取的 MAC 地址。此选项严格限定为测试用途。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:575`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L575)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED"></a>

## 193.49 `CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED`

**提示（Prompt）**：固定 MAC 地址（fixed MAC address）

**说明（Help）**

启用固定 MAC 地址（fixed MAC address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_MAC_ADDRESS>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:592`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L592)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi MAC 地址类型（MAC address type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_MAC_ADDRESS)。

<a id="CONFIG_WIFI_HWSIM"></a>

## 193.50 `CONFIG_WIFI_HWSIM`

**提示（Prompt）**：虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**说明（Help）**

注册 N 个由进程内帧中继总线（in-process frame relay bus）支持的虚拟 Wi-Fi 接口。用于在 `native_sim` 上测试 `hostapd` 和 `wpa_supplicant`，无需真实硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI && CONFIG_NET_L2_ETHERNET && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)。

<a id="CONFIG_WIFI_HWSIM_CONNECT_TIMEOUT_SEC"></a>

## 193.51 `CONFIG_WIFI_HWSIM_CONNECT_TIMEOUT_SEC`

**提示（Prompt）**：连接超时（Connect timeout），单位为秒，用于测试

**说明（Help）**

自动化测试中等待连接结果（connect result）的最长时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[1, 120]
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_DEFAULT_CHANNEL"></a>

## 193.52 `CONFIG_WIFI_HWSIM_DEFAULT_CHANNEL`

**提示（Prompt）**：默认信道（Default channel，2.4 GHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[1, 14]
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_DEFAULT_SIGNAL_DBM"></a>

## 193.53 `CONFIG_WIFI_HWSIM_DEFAULT_SIGNAL_DBM`

**提示（Prompt）**：默认模拟接收信号强度指示（RSSI），单位为 dBm

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
-50
```

**取值范围（Ranges）**

```text
[-100, -10]
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_MEM_SLAB_COUNT"></a>

## 193.54 `CONFIG_WIFI_HWSIM_MEM_SLAB_COUNT`

**提示（Prompt）**：帧池（Frame pool）大小，以帧数表示

**说明（Help）**

`k_mem_slab` 内存块池中 `struct hwsim_frame` 条目的数量。每个条目保存一个在途帧（in-flight frame，最大 `HWSIM_FRAME_MTU` 字节）及该帧的元数据（metadata）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_NUM_RADIOS"></a>

## 193.55 `CONFIG_WIFI_HWSIM_NUM_RADIOS`

**提示（Prompt）**：虚拟无线电设备（virtual radios）数量

**说明（Help）**

每个无线电设备（radio）对应一个 `net_if`。最少为 2 个，即一个接入点（AP）和一个站点（STA）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_RX_STACK_SIZE"></a>

## 193.56 `CONFIG_WIFI_HWSIM_RX_STACK_SIZE`

**提示（Prompt）**：每个无线电设备的接收线程（RX thread）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_HWSIM_SHELL"></a>

## 193.57 `CONFIG_WIFI_HWSIM_SHELL`

**提示（Prompt）**：hwsim 命令行命令（shell commands）

**说明（Help）**

提供 `hwsim channel/signal/loss/dump` shell 命令，在交互式测试中用于手动故障注入（fault injection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/hwsim/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/hwsim/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_INIT_PRIORITY"></a>

## 193.58 `CONFIG_WIFI_INIT_PRIORITY`

**提示（Prompt）**：Wi-Fi 驱动初始化优先级（init priority）

**说明（Help）**

Wi-Fi 设备驱动初始化优先级（initialization priority）。除非清楚修改的影响，否则不要更改。注意：其优先级数值需要低于网络协议栈，才能在网络子系统（networking subsystem）之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI
```

**默认值（Defaults）**

```text
86 if CONFIG_WIFI_AIROC && CONFIG_AIROC_WIFI_BUS_SDIO
87 if CONFIG_WIFI_ESP_HOSTED_MCU && CONFIG_ESP_HOSTED_MCU_SDIO
80
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_AIROC_WIFI_BUS_SDIO`](P188_drivers_wifi_配置项参考_1.md#CONFIG_AIROC_WIFI_BUS_SDIO)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_ESP_HOSTED_MCU_SDIO`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU_SDIO)。

<a id="CONFIG_WIFI_MAC_ADDRESS"></a>

## 193.59 `CONFIG_WIFI_MAC_ADDRESS`

**提示（Prompt）**：Wi-Fi MAC 地址类型（MAC address type）

**说明（Help）**

选择 Wi-Fi 驱动使用的 MAC 地址类型（MAC address type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED if CONFIG_WIFI_FIXED_MAC_ADDRESS != ""
CONFIG_WIFI_OTP_MAC_ADDRESS
```

**可选项（Choices）**

```text
CONFIG_WIFI_OTP_MAC_ADDRESS
CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED
CONFIG_WIFI_RANDOM_MAC_ADDRESS
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:580`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L580)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_FIXED_MAC_ADDRESS_ENABLED)、[`CONFIG_WIFI_FIXED_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_FIXED_MAC_ADDRESS)、[`CONFIG_WIFI_OTP_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OTP_MAC_ADDRESS)、[`CONFIG_WIFI_RANDOM_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_RANDOM_MAC_ADDRESS)。

<a id="CONFIG_WIFI_NATIVE_SIM"></a>

## 193.60 `CONFIG_WIFI_NATIVE_SIM`

**提示（Prompt）**：面向 native-sim 开发板的简单 Wi-Fi 驱动

**说明（Help）**

启用 native-sim Wi-Fi 支持。目前仅可用于简单验证 hostap API 等接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && !CONFIG_64BIT && CONFIG_WIFI_NM_WPA_SUPPLICANT && DT_HAS_ZEPHYR_NATIVE_SIM_WIFI_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_NET_INTERFACE_NAME
```

**定义位置（Location）**：[`drivers/wifi/native_sim/Kconfig.native_sim:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/native_sim/Kconfig.native_sim#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_NET_INTERFACE_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_INTERFACE_NAME)。

<a id="CONFIG_WIFI_NATIVE_SIM_RX_WAIT_TIME"></a>

## 193.61 `CONFIG_WIFI_NATIVE_SIM_RX_WAIT_TIME`

**提示（Prompt）**：Wi-Fi 接收超时（RX timeout），单位为 ms

**说明（Help）**

Native sim Wi-Fi 驱动会反复检查是否有新数据。此项指定在没有新数据时，线程在两次检查之间休眠的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NATIVE_SIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`drivers/wifi/native_sim/Kconfig.native_sim:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/native_sim/Kconfig.native_sim#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 面向 native-sim 开发板的简单 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NATIVE_SIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NATIVE_SIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_NATIVE_SIM_SUPPLICANT_LOG_FILE"></a>

## 193.62 `CONFIG_WIFI_NATIVE_SIM_SUPPLICANT_LOG_FILE`

**提示（Prompt）**：`zephyr-host-wpa_supplicant.log`

**说明（Help）**

用于主机侧输出（host side output）的 `wpa_supplicant` 日志文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NATIVE_SIM && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/native_sim/Kconfig.native_sim:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/native_sim/Kconfig.native_sim#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 面向 native-sim 开发板的简单 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NATIVE_SIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NATIVE_SIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_NRF70"></a>

## 193.63 `CONFIG_WIFI_NRF70`

**提示（Prompt）**：nRF70 驱动

**说明（Help）**

Nordic Wi-Fi 驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NORDIC_NRF7002_SPI_ENABLED || DT_HAS_NORDIC_NRF7002_QSPI_ENABLED || DT_HAS_NORDIC_NRF7001_SPI_ENABLED || DT_HAS_NORDIC_NRF7001_QSPI_ENABLED || DT_HAS_NORDIC_NRF7000_SPI_ENABLED || DT_HAS_NORDIC_NRF7000_QSPI_ENABLED) && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT if CONFIG_NETWORKING
CONFIG_NET_L2_ETHERNET_MGMT if CONFIG_NETWORKING && CONFIG_NET_L2_ETHERNET
CONFIG_WIFI_USE_NATIVE_NETWORKING if CONFIG_NETWORKING
CONFIG_NRF70_BUSLIB
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED if CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_NRF70_BUSLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_BUSLIB)、[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)。

<a id="CONFIG_WIFI_NRF70_SCAN_DISABLE_DFS_CHANNELS"></a>

## 193.64 `CONFIG_WIFI_NRF70_SCAN_DISABLE_DFS_CHANNELS`

**提示（Prompt）**：在扫描操作中禁用动态频率选择信道（DFS channels）

**说明（Help）**

扫描操作中不包含动态频率选择信道（DFS channels）。由于 DFS 信道很少使用，此选项有助于缩短扫描时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:739`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L739)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_NRF70_SCAN_TIMEOUT_S"></a>

## 193.65 `CONFIG_WIFI_NRF70_SCAN_TIMEOUT_S`

**提示（Prompt）**：扫描超时（Scan timeout），单位为秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:704`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L704)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_NRF70_SKIP_LOCAL_ADMIN_MAC"></a>

## 193.66 `CONFIG_WIFI_NRF70_SKIP_LOCAL_ADMIN_MAC`

**提示（Prompt）**：从扫描结果中隐藏以非独立 MAC 地址作为 BSSID 的网络

**说明（Help）**

Wi-Fi 接入点（access points）使用本地管理 MAC 地址（locally administered MAC addresses）管理多个虚拟接口。对于地理定位（geo-location）场景，这些虚拟接口的网络没有帮助，因为它们与具有全局唯一 MAC 地址的主接口位于同一位置。因此，为节省资源，此选项会从扫描结果中丢弃这些网络。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:730`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L730)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_NXP"></a>

## 193.67 `CONFIG_WIFI_NXP`

**提示（Prompt）**：NXP Wi-Fi 驱动支持

**说明（Help）**

启用 NXP SoC 的 Wi-Fi 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_WIFI_ENABLED && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_ETHERNET_MGMT
CONFIG_SDHC if !CONFIG_SOC_SERIES_RW6XX
CONFIG_SDIO_STACK if !CONFIG_SOC_SERIES_RW6XX
CONFIG_WIFI_NM
CONFIG_EVENTS
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_ETHERNET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SDIO_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDIO_STACK)、[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RW6XX`。

<a id="CONFIG_WIFI_OFFLOAD"></a>

## 193.68 `CONFIG_WIFI_OFFLOAD`

**提示（Prompt）**：支持卸载型 Wi-Fi 设备驱动（offloaded Wi-Fi device drivers）

**说明（Help）**

启用对全 MAC Wi-Fi 设备（Full-MAC Wi-Fi devices）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_NET_OFFLOAD
```

**被选择（Selected by）**

```text
CONFIG_WIFI_ESP_AT
CONFIG_WIFI_ESWIFI
CONFIG_WIFI_SIMPLELINK
CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_OFFLOAD
CONFIG_WIFI_WINC1500
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_OFFLOAD)、[`CONFIG_WIFI_WINC1500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_WINC1500)。

<a id="CONFIG_WIFI_OTP_MAC_ADDRESS"></a>

## 193.69 `CONFIG_WIFI_OTP_MAC_ADDRESS`

**提示（Prompt）**：使用一次性可编程存储器（OTP）中的 MAC 地址

**说明（Help）**

使用 nRF70 的一次性可编程存储器（OTP memory）中保存的 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_MAC_ADDRESS>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:587`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L587)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi MAC 地址类型（MAC address type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_MAC_ADDRESS)。

<a id="CONFIG_WIFI_RANDOM_MAC_ADDRESS"></a>

## 193.70 `CONFIG_WIFI_RANDOM_MAC_ADDRESS`

**提示（Prompt）**：运行时生成随机 MAC 地址（Random MAC address）

**说明（Help）**

启用运行时随机 MAC 地址生成（random MAC address generation）。随机 MAC 地址由熵设备（entropy device）的随机数生成器生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_GENERATOR && <choice CONFIG_WIFI_MAC_ADDRESS>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi MAC 地址类型（MAC address type）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_WIFI_MAC_ADDRESS`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_MAC_ADDRESS)。

<a id="CONFIG_WIFI_SILABS_SIWX91X"></a>

## 193.71 `CONFIG_WIFI_SILABS_SIWX91X`

**提示（Prompt）**：Silabs SiWx91x Wi-Fi 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的 Wi-Fi 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_WIFI_ENABLED && CONFIG_NETWORKING && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_EVENTS
CONFIG_NET_L2_WIFI_MGMT
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_ACTIVE_SCAN_DURATION"></a>

## 193.72 `CONFIG_WIFI_SILABS_SIWX91X_ADV_ACTIVE_SCAN_DURATION`

**提示（Prompt）**：高级主动扫描时长（Advanced active scan duration），单位为 ms

**说明（Help）**

配置 Wi-Fi 扫描默认的高级主动扫描时长（advanced active scan duration）。此值决定高级主动扫描在每个信道停留的时间，单位为毫秒。可根据网络环境调整此值，以优化扫描速度和准确性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_MULTIPROBE"></a>

## 193.73 `CONFIG_WIFI_SILABS_SIWX91X_ADV_MULTIPROBE`

**提示（Prompt）**：高级多探测设置（Advanced multiprobe setting）

**说明（Help）**

配置 Wi-Fi 扫描的高级多探测设置（advanced multiprobe setting）。设为 `1` 时，扫描期间除已连接的 SSID 外，还会向所有接入点发送多个探测请求（probe requests）。可根据网络需求调整此值，细化扫描行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_PASSIVE_SCAN_DURATION"></a>

## 193.74 `CONFIG_WIFI_SILABS_SIWX91X_ADV_PASSIVE_SCAN_DURATION`

**提示（Prompt）**：高级被动扫描时长（Advanced passive scan duration），单位为 ms

**说明（Help）**

配置 Wi-Fi 扫描默认的高级被动扫描时长（advanced passive scan duration）。此值决定高级被动扫描在每个信道停留的时间，单位为毫秒。可根据网络环境调整此值，以优化扫描速度和准确性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_RSSI_TOLERANCE_THRESHOLD"></a>

## 193.75 `CONFIG_WIFI_SILABS_SIWX91X_ADV_RSSI_TOLERANCE_THRESHOLD`

**提示（Prompt）**：高级 RSSI 容差阈值（Advanced RSSI tolerance threshold），单位为 dBm

**说明（Help）**

配置高级 Wi-Fi 扫描默认的接收信号强度指示容差阈值（RSSI tolerance threshold）。此值决定高级扫描期间可接受的信号强度变化，单位为 dBm。可调整此值，细化扫描机制对信号波动的敏感度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_SCAN_PERIODICITY"></a>

## 193.76 `CONFIG_WIFI_SILABS_SIWX91X_ADV_SCAN_PERIODICITY`

**提示（Prompt）**：高级扫描周期（Advanced scan periodicity），单位为 ms

**说明（Help）**

配置 Wi-Fi 扫描默认的高级扫描周期（advanced scan periodicity）。此值决定连续两次高级扫描的间隔，单位为毫秒。可根据网络环境调整此值，以平衡扫描频率和功耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ADV_SCAN_THRESHOLD"></a>

## 193.77 `CONFIG_WIFI_SILABS_SIWX91X_ADV_SCAN_THRESHOLD`

**提示（Prompt）**：高级扫描阈值（Advanced scan threshold），单位为 dBm

**说明（Help）**

配置 Wi-Fi 扫描默认的高级扫描阈值（advanced scan threshold）。此值指定触发高级扫描机制的信号强度阈值，单位为 dBm；信号强度低于该值时触发。可根据网络环境调整此值，以优化扫描行为。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
-40
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING"></a>

## 193.78 `CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING`

**提示（Prompt）**：Wi-Fi 漫游（roaming）支持

**说明（Help）**

启用此选项以配置漫游参数（roaming parameters）。后台扫描（background scan）生效时会自动启用漫游，以改善接入点切换过程中的连接性和性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ENHANCED_MAX_PSP"></a>

## 193.79 `CONFIG_WIFI_SILABS_SIWX91X_ENHANCED_MAX_PSP`

**提示（Prompt）**：增强型最大 PSP 支持（Enhanced Max PSP Support）

**说明（Help）**

使用增强型节能轮询算法（PS-Poll algorithm）替代通常的快速节能模式（Fast PS，有时也称动态节能 Dynamic PS）。该算法会检测接入点（AP）是否未能正确处理 PS-Poll 请求，出现这种情况时切换到 Dynamic PS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_FEAT_SECURITY_PSK"></a>

## 193.80 `CONFIG_WIFI_SILABS_SIWX91X_FEAT_SECURITY_PSK`

**提示（Prompt）**：WPA／WPA2 预共享密钥安全支持（PSK Security Support）

**说明（Help）**

在客户端模式（client mode）下启用基于预共享密钥（PSK）的 WPA／WPA2 安全机制。建议需要 WPA、WPA2 或混合安全模式（mixed security modes）的配置启用。禁用此功能可减少数据缓冲区用量，因而可能提高吞吐量（throughput）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_LIMIT_PACKET_BUF_PER_STA"></a>

## 193.81 `CONFIG_WIFI_SILABS_SIWX91X_LIMIT_PACKET_BUF_PER_STA`

**提示（Prompt）**：限制接入点模式（AP mode）下每个站点（STA）的缓冲数据包数量

**说明（Help）**

在接入点模式（AP mode）下，如果设置此位，当站点（Station，STA）处于节能模式（Power Save，PS）时，每个 STA 仅缓冲两个数据包。这有助于管理缓冲区用量并确保高效处理数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_MFP"></a>

## 193.82 `CONFIG_WIFI_SILABS_SIWX91X_MFP`

**提示（Prompt）**：802.11w 管理帧保护（Management Frame Protection，MFP）支持

**说明（Help）**

启用 IEEE 802.11w 管理帧保护（Management Frame Protection，MFP），以安全地处理管理帧。

注意：

- WPA3-Personal 和 WPA3-Transition 模式需要此功能。
- 禁用此功能会释放 MFP 使用的内存，可使 TCP 吞吐量提高约 10～12%（约 1～2 Mbps）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE"></a>

## 193.83 `CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE`

**提示（Prompt）**：原生（Native）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动 → 网络协议栈（Network stack）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_OFFLOAD"></a>

## 193.84 `CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_OFFLOAD`

**提示（Prompt）**：卸载（Offloaded）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_WIFI_OFFLOAD
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动 → 网络协议栈（Network stack）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ROAMING_TRIGGER_LEVEL"></a>

## 193.85 `CONFIG_WIFI_SILABS_SIWX91X_ROAMING_TRIGGER_LEVEL`

**提示（Prompt）**：默认漫游触发电平（roam trigger level），单位为 dBm

**说明（Help）**

设置默认漫游触发电平（roam trigger level）。较大的值会较早触发漫游，较小的值会延后触发。它决定何时开始搜索新的接入点（AP）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING && CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
-70
```

**取值范围（Ranges）**

```text
[-100, -10]
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动 → Wi-Fi 漫游（roaming）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING)、[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ROAMING_TRIGGER_LEVEL_CHANGE"></a>

## 193.86 `CONFIG_WIFI_SILABS_SIWX91X_ROAMING_TRIGGER_LEVEL_CHANGE`

**提示（Prompt）**：默认漫游触发电平变化量（roam trigger level change），单位为 dBm

**说明（Help）**

配置 Wi-Fi 漫游默认的触发电平变化量（trigger level change）。此值决定发起漫游事件所需的信号强度变化，单位为 dBm。较小的值可能使漫游行为更敏感，较大的值则可能减少漫游事件发生频率。它决定切换到新接入点（AP）所需的信号差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING && CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 90]
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动 → Wi-Fi 漫游（roaming）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING)、[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SILABS_SIWX91X_ROAMING_USE_DEAUTH"></a>

## 193.87 `CONFIG_WIFI_SILABS_SIWX91X_ROAMING_USE_DEAUTH`

**提示（Prompt）**：使用解除认证帧（deauth frames）进行漫游

**说明（Help）**

启用此选项，允许使用解除认证帧（deauthentication frames）进行漫游（roaming）。默认使用空数据包（Null data packets）进行漫游。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING && CONFIG_WIFI_SILABS_SIWX91X && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/siwx91x/Kconfig.siwx91x:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/Kconfig.siwx91x#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Silabs SiWx91x Wi-Fi 驱动 → Wi-Fi 漫游（roaming）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_ENABLE_ROAMING)、[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SIMPLELINK"></a>

## 193.88 `CONFIG_WIFI_SIMPLELINK`

**提示（Prompt）**：SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**说明（Help）**

此卸载型 Wi-Fi 驱动（offloaded WiFi driver）已弃用，将在后续版本中移除。此官方快照计划在 Zephyr 4.6 中移除该驱动。弃用原因是该驱动已无人维护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_SIMPLELINK_HOST_DRIVER
CONFIG_WIFI_OFFLOAD
CONFIG_NET_L2_WIFI_MGMT
CONFIG_ZVFS
CONFIG_ZVFS_FDTABLE
CONFIG_POSIX_SEMAPHORES
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_SIMPLELINK_HOST_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SIMPLELINK_HOST_DRIVER)、[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_ZVFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS)、[`CONFIG_ZVFS_FDTABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_FDTABLE)、[`CONFIG_POSIX_SEMAPHORES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_WIFI_SIMPLELINK_FAST_CONNECT_TIMEOUT"></a>

## 193.89 `CONFIG_WIFI_SIMPLELINK_FAST_CONNECT_TIMEOUT`

**提示（Prompt）**：启动时等待快速连接（fast connect）的时间，单位为秒

**说明（Help）**

SimpleLink 在启动时使用 `FastConnect` 功能重新连接此前连接的接入点（AP）。如果 Wi-Fi 连接超时，SimpleLink 驱动将初始化失败，并记录错误日志（LOG）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SIMPLELINK && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SIMPLELINK_MAX_PACKET_SIZE"></a>

## 193.90 `CONFIG_WIFI_SIMPLELINK_MAX_PACKET_SIZE`

**提示（Prompt）**：数据包最大大小（Maximum size of a packet），单位为字节

**说明（Help）**

设置经过芯片的网络数据包的最大大小。此值决定每个缓冲区池（buffer pool）中各个缓冲区的大小。除非清楚修改的影响，否则不要更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SIMPLELINK && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1472
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SIMPLELINK_MAX_SCAN_RETRIES"></a>

## 193.91 `CONFIG_WIFI_SIMPLELINK_MAX_SCAN_RETRIES`

**提示（Prompt）**：获取网络扫描表（network scan table）的重试次数

**说明（Help）**

重试请求网络列表（network list）的次数，各次重试之间间隔一秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SIMPLELINK && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SIMPLELINK_NAME"></a>

## 193.92 `CONFIG_WIFI_SIMPLELINK_NAME`

**提示（Prompt）**：驱动名称（Driver name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SIMPLELINK && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"SimpleLink"
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_SIMPLELINK_SCAN_COUNT"></a>

## 193.93 `CONFIG_WIFI_SIMPLELINK_SCAN_COUNT`

**提示（Prompt）**：网络扫描表条目数（network scan table entries），最大 30

**说明（Help）**

一次 Wi-Fi 扫描操作请求的结果数量。实际返回数量可能更少，最大为 30。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SIMPLELINK && CONFIG_WIFI
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`drivers/wifi/simplelink/Kconfig.simplelink:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/simplelink/Kconfig.simplelink#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → SimpleLink Wi-Fi 驱动支持［已弃用，DEPRECATED］

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ST67W611M1"></a>

## 193.94 `CONFIG_WIFI_ST67W611M1`

**提示（Prompt）**：ST67W611M1 Wi-Fi 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_ST67W611M1_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_MODEM
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_CMD_HANDLER
CONFIG_GPIO
CONFIG_SPI
CONFIG_SPI_STM32_DMA if CONFIG_SOC_FAMILY_STM32 && n
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_WIFI_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_CONTEXT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_CMD_HANDLER`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CMD_HANDLER)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_STM32_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32_DMA)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_WIFI_USAGE_MODE"></a>

## 193.95 `CONFIG_WIFI_USAGE_MODE`

**提示（Prompt）**：应用对 Wi-Fi 驱动的使用方式（Application usage）

**说明（Help）**

告知 Wi-Fi 驱动应用将使用哪些 Wi-Fi 功能。驱动可根据此选择，为相应的驱动专用选项（driver-specific options）设置合适的默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_USAGE_MODE_STA
```

**可选项（Choices）**

```text
CONFIG_WIFI_USAGE_MODE_STA
CONFIG_WIFI_USAGE_MODE_AP
CONFIG_WIFI_USAGE_MODE_STA_AP
CONFIG_WIFI_USAGE_MODE_SCAN_ONLY
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_STA`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA)、[`CONFIG_WIFI_USAGE_MODE_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_AP)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_USAGE_MODE_SCAN_ONLY`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_SCAN_ONLY)。

<a id="CONFIG_WIFI_USAGE_MODE_AP"></a>

## 193.96 `CONFIG_WIFI_USAGE_MODE_AP`

**提示（Prompt）**：Wi-Fi 接口充当接入点（Access Point）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_USAGE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 应用对 Wi-Fi 驱动的使用方式（Application usage）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_USAGE_MODE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE)。

<a id="CONFIG_WIFI_USAGE_MODE_SCAN_ONLY"></a>

## 193.97 `CONFIG_WIFI_USAGE_MODE_SCAN_ONLY`

**提示（Prompt）**：Wi-Fi 接口仅用于 SSID 扫描（scanning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_USAGE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 应用对 Wi-Fi 驱动的使用方式（Application usage）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_USAGE_MODE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE)。

<a id="CONFIG_WIFI_USAGE_MODE_STA"></a>

## 193.98 `CONFIG_WIFI_USAGE_MODE_STA`

**提示（Prompt）**：Wi-Fi 接口充当站点（Station）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_USAGE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 应用对 Wi-Fi 驱动的使用方式（Application usage）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_USAGE_MODE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE)。

<a id="CONFIG_WIFI_USAGE_MODE_STA_AP"></a>

## 193.99 `CONFIG_WIFI_USAGE_MODE_STA_AP`

**提示（Prompt）**：Wi-Fi 接口同时充当接入点（Access Point）和站点（Station）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_USAGE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 应用对 Wi-Fi 驱动的使用方式（Application usage）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_USAGE_MODE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE)。

<a id="CONFIG_WIFI_USE_NATIVE_NETWORKING"></a>

## 193.100 `CONFIG_WIFI_USE_NATIVE_NETWORKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择此隐藏配置项（hidden configuration）后，Wi-Fi 驱动可使用原生以太网协议栈接口（native Ethernet stack interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI
```

**被选择（Selected by）**

```text
CONFIG_WIFI_AMEBA
CONFIG_WIFI_BFLB
CONFIG_WIFI_ESP32
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESP_HOSTED_MCU
CONFIG_WIFI_HWSIM
CONFIG_WIFI_AIROC
CONFIG_WIFI_NATIVE_SIM
CONFIG_WIFI_NRF70
CONFIG_WIFI_NXP
CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE
CONFIG_WIFI_ST67W611M1
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI_NATIVE_SIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NATIVE_SIM)、[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE)、[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)。

<!-- kconfig-navigation -->

[上一章](P192_drivers_wifi_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P194_drivers_wifi_配置项参考_7.md)
