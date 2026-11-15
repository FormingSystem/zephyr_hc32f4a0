---
id: learning.zephyr-docs.kconfig-reference.page-189
title: "`drivers/wifi`配置项参考（2/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第189章\_`drivers/wifi`配置项参考（2/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP32_WIFI_STA_POWER_SAVE_MAX_MODEM"></a>

## 189.1 `CONFIG_ESP32_WIFI_STA_POWER_SAVE_MAX_MODEM`

**提示（Prompt）**：最大调制解调器睡眠（Maximum Modem Sleep）

**说明（Help）**

站点每个监听间隔（Listen Interval）唤醒一次以接收信标。默认监听间隔为 3 个信标间隔，可通过 Wi-Fi 节能管理请求（Power Save Management Request）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:433`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L433)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 站点节能模式（Station Power Save Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE)。

<a id="CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM"></a>

## 189.2 `CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM`

**提示（Prompt）**：最小调制解调器睡眠（Minimum Modem Sleep）

**说明（Help）**

站点每个投递流量指示消息（DTIM）周期唤醒一次以接收信标。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 站点节能模式（Station Power Save Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE)。

<a id="CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE"></a>

## 189.3 `CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE`

**提示（Prompt）**：站点节能模式（Station Power Save Mode）

**说明（Help）**

驱动启动时应用于站点接口的节能模式（Power Save Mode）。仍可在运行时通过 Wi-Fi 节能管理请求修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM
```

**可选项（Choices）**

```text
CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM
CONFIG_ESP32_WIFI_STA_POWER_SAVE_MAX_MODEM
CONFIG_ESP32_WIFI_STA_POWER_SAVE_NONE
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_MIN_MODEM)、[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_MAX_MODEM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_MAX_MODEM)、[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_NONE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_NONE)。

<a id="CONFIG_ESP32_WIFI_STA_POWER_SAVE_NONE"></a>

## 189.4 `CONFIG_ESP32_WIFI_STA_POWER_SAVE_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

调制解调器永不睡眠。提供最低延迟和最高吞吐量，代价是持续消耗活动状态电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 站点节能模式（Station Power Save Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP32_WIFI_STA_POWER_SAVE_MODE)。

<a id="CONFIG_ESP32_WIFI_STA_RECONNECT"></a>

## 189.5 `CONFIG_ESP32_WIFI_STA_RECONNECT`

**提示（Prompt）**：Wi-Fi 连接重试（Connection Retry）

**说明（Help）**

设置 Wi-Fi 在断开连接后自动重新连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_STA_SCAN_ALL"></a>

## 189.6 `CONFIG_ESP32_WIFI_STA_SCAN_ALL`

**提示（Prompt）**：站点模式连接时扫描所有可用接入点（AP）

**说明（Help）**

在站点模式下连接时，扫描所有信道，并连接接收信号强度指示（RSSI）最高的信道。未启用时，执行快速扫描，连接找到的第一个 AP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_STA_START_TIMEOUT"></a>

## 189.7 `CONFIG_ESP32_WIFI_STA_START_TIMEOUT`

**提示（Prompt）**：Wi-Fi 站点启动等待超时（ms）

**说明（Help）**

连接请求等待站点已启动事件（Station-started Event）的最长时间；该事件由事件任务处理，超时后连接请求放弃。如果事件负载较重时连接因站点尚未进入站点模式而失败，可增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_SUITE_B"></a>

## 189.8 `CONFIG_ESP32_WIFI_SUITE_B`

**提示（Prompt）**：WPA3 企业模式 Suite-B 支持

**说明（Help）**

启用 WPA3 企业模式（WPA3-Enterprise）Suite-B 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_GCMP_SUPPORT
CONFIG_ESP32_WIFI_GMAC_SUPPORT
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:795`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L795)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_GCMP_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_GCMP_SUPPORT)、[`CONFIG_ESP32_WIFI_GMAC_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_GMAC_SUPPORT)。

<a id="CONFIG_ESP32_WIFI_SUITE_B_192"></a>

## 189.9 `CONFIG_ESP32_WIFI_SUITE_B_192`

**提示（Prompt）**：WPA3 企业模式 Suite-B 192 位支持

**说明（Help）**

启用 WPA3 企业模式（WPA3-Enterprise）192 位 Suite-B 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENTERPRISE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_GCMP_SUPPORT
CONFIG_ESP32_WIFI_GMAC_SUPPORT
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
CONFIG_PSA_WANT_ECC_SECP_R1_384
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:804`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L804)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA2/WPA3 企业模式（Enterprise）站点支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_GCMP_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_GCMP_SUPPORT)、[`CONFIG_ESP32_WIFI_GMAC_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_GMAC_SUPPORT)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)、[`CONFIG_PSA_WANT_ECC_SECP_R1_384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ECC_SECP_R1_384)。

<a id="CONFIG_ESP32_WIFI_TASK_STACK_SIZE"></a>

## 189.10 `CONFIG_ESP32_WIFI_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 任务栈大小下限（Floor）

**说明（Help）**

Wi-Fi 库二进制组件（Blobs）创建的 Wi-Fi 任务的最小栈大小。实际使用的栈大小取此值与二进制组件运行时请求的栈深度中的较大者，因此增大此 Kconfig 值只是提高下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
3584
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_TX_BA_WIN"></a>

## 189.11 `CONFIG_ESP32_WIFI_TX_BA_WIN`

**提示（Prompt）**：Wi-Fi A-MPDU 发送块确认（TX BA）窗口大小

**说明（Help）**

设置 Wi-Fi 块确认发送窗口（Block Ack TX Window）的大小。通常较大的值可提高吞吐量，但也占用更多内存。除非有特殊原因，例如用 iperf 测试最大 UDP 发送吞吐量，否则通常不应修改默认值。在屏蔽箱（Shieldbox）内进行 iperf 测试时，推荐值为 9 至 12。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_AMPDU_TX_ENABLED && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[2, 32]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 聚合 MAC 协议数据单元发送（A-MPDU TX）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_AMPDU_TX_ENABLED`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_AMPDU_TX_ENABLED)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_TX_BUFFER"></a>

## 189.12 `CONFIG_ESP32_WIFI_TX_BUFFER`

**提示（Prompt）**：Wi-Fi 发送（TX）缓冲区类型

**说明（Help）**

选择 Wi-Fi 发送（TX）缓冲区类型：

- 静态（Static）：Wi-Fi 初始化时分配，反初始化时释放。每个静态发送缓冲区大小固定，约为 1.6 KB。
- 动态（Dynamic）：TCP/IP 协议栈向 Wi-Fi 驱动交付数据帧时，按需分配发送缓冲区；Wi-Fi 驱动发送完成后释放。每个动态发送缓冲区大小取决于 TCP/IP 层发送的数据帧长度。

启用伪静态 RAM（PSRAM）时，应选择静态，以保证有足够的 Wi-Fi 发送缓冲区。未启用 PSRAM 时，应选择动态，以提高 RAM 利用率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER
```

**可选项（Choices）**

```text
CONFIG_ESP32_WIFI_STATIC_TX_BUFFER
CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_DYNAMIC_TX_BUFFER)、[`CONFIG_ESP32_WIFI_STATIC_TX_BUFFER`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_STATIC_TX_BUFFER)。

<a id="CONFIG_ESP32_WIFI_TX_RETRY_TIMEOUT_MS"></a>

## 189.13 `CONFIG_ESP32_WIFI_TX_RETRY_TIMEOUT_MS`

**提示（Prompt）**：Wi-Fi 发送（TX）重试超时（ms）

**说明（Help）**

发送操作等待前述某个发送缓冲区释放的最长时间，超过后丢弃数据包。该等待会阻塞调用线程，因此超时值也限制额外延迟。设为 0 表示立即丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
50
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_WNM_SUPPORT"></a>

## 189.14 `CONFIG_ESP32_WIFI_WNM_SUPPORT`

**提示（Prompt）**：802.11v 基本服务集转换管理（BSS Transition Management）

**说明（Help）**

基本服务集转换管理（BSS Transition Management，BTM）允许 AP 请求站点移动到指定 AP，或告诉站点哪些 AP 更受偏好。只实现对网络辅助漫游（Network-assisted Roaming）有用的操作。启用后，站点在关联时声明 BTM 能力，AP 在发送 BSS 转换管理请求前会检查该能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_11KV_SUPPORT && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:850`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L850)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → 802.11k 和 802.11v 支持

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_11KV_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_11KV_SUPPORT)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP32_WIFI_WPA3_COMPATIBLE"></a>

## 189.15 `CONFIG_ESP32_WIFI_WPA3_COMPATIBLE`

**提示（Prompt）**：WPA3 过渡模式兼容性（Transition Mode Compatibility）

**说明（Help）**

启用 WPA3 兼容模式，以便与在 WPA2/WPA3 过渡期间使用 RSNXE 覆盖（RSNXE Override）的 AP 互操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:1021`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L1021)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → WPA3 个人模式（WPA3-Personal）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENABLE_WPA3_SAE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_ESP_WIFI_HEAP"></a>

## 189.16 `CONFIG_ESP_WIFI_HEAP`

**提示（Prompt）**：Wi-Fi 适配器堆内存（Adapter Heap Memory）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_ESP_WIFI_HEAP_SYSTEM
```

**可选项（Choices）**

```text
CONFIG_ESP_WIFI_HEAP_SYSTEM
CONFIG_ESP_WIFI_HEAP_SPIRAM
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP_WIFI_HEAP_SYSTEM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP_SYSTEM)、[`CONFIG_ESP_WIFI_HEAP_SPIRAM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP_SPIRAM)。

<a id="CONFIG_ESP_WIFI_HEAP_SPIRAM"></a>

## 189.17 `CONFIG_ESP_WIFI_HEAP_SPIRAM`

**提示（Prompt）**：Wi-Fi 适配器使用 SPI RAM 内存池堆（`smh_malloc`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_WIFI_HEAP>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 适配器堆内存（Adapter Heap Memory）

**配置项引用（Symbol References）**：[`CONFIG_ESP_WIFI_HEAP`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP)。

<a id="CONFIG_ESP_WIFI_HEAP_SYSTEM"></a>

## 189.18 `CONFIG_ESP_WIFI_HEAP_SYSTEM`

**提示（Prompt）**：Wi-Fi 适配器使用内核内存池堆（`k_malloc`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_WIFI_HEAP>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → Wi-Fi 适配器堆内存（Adapter Heap Memory）

**配置项引用（Symbol References）**：[`CONFIG_ESP_WIFI_HEAP`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_AMEBA_WIFI"></a>

## 189.19 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_AMEBA_WIFI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

增加堆内存池（Heap Memory Pool），用于分配 Ameba Wi-Fi 扫描缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_ESP_WIFI"></a>

## 189.20 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_ESP_WIFI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

确保 Wi-Fi 驱动有最低所需堆容量，可容纳默认数量的 Wi-Fi 缓冲区。静态接收（RX）缓冲区默认数量为 10；每多增加一个，系统堆约多消耗 1.6 KB，因此应相应增大 `CONFIG_HEAP_MEM_POOL_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
51200 if CONFIG_ESP_WIFI_HEAP_SYSTEM
25400 if CONFIG_ESP_WIFI_HEAP_SPIRAM
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_ESP_WIFI_HEAP_SYSTEM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP_SYSTEM)、[`CONFIG_ESP_WIFI_HEAP_SPIRAM`](P189_drivers_wifi_配置项参考_2.md#CONFIG_ESP_WIFI_HEAP_SPIRAM)。

<a id="CONFIG_IFX_WIFI_SOFTAP_SUPPORT"></a>

## 189.21 `CONFIG_IFX_WIFI_SOFTAP_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在驱动中启用 Wi-Fi 软件接入点（SoftAP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_ANT_GAIN_2G"></a>

## 189.22 `CONFIG_NRF70_ANT_GAIN_2G`

**提示（Prompt）**：2.4 GHz 频段天线增益（Antenna Gain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 6]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_ANT_GAIN_5G_BAND1"></a>

## 189.23 `CONFIG_NRF70_ANT_GAIN_5G_BAND1`

**提示（Prompt）**：5 GHz 频段（5150 MHz 至 5350 MHz）天线增益（Antenna Gain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 6]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:337`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L337)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_ANT_GAIN_5G_BAND2"></a>

## 189.24 `CONFIG_NRF70_ANT_GAIN_5G_BAND2`

**提示（Prompt）**：5 GHz 频段（5470 MHz 至 5730 MHz）天线增益（Antenna Gain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 6]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_ANT_GAIN_5G_BAND3"></a>

## 189.25 `CONFIG_NRF70_ANT_GAIN_5G_BAND3`

**提示（Prompt）**：5 GHz 频段（5730 MHz 至 5895 MHz）天线增益（Antenna Gain）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 6]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L347)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_AP_MODE"></a>

## 189.26 `CONFIG_NRF70_AP_MODE`

**提示（Prompt）**：接入点模式（Access Point Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NRF7002 || CONFIG_WIFI_NRF7001) && CONFIG_WIFI_NM_WPA_SUPPLICANT_AP && CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_AP || CONFIG_WIFI_USAGE_MODE_STA_AP
```

**主动选择（Selects）**

```text
CONFIG_NRF70_DATA_TX
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF7002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7002)、[`CONFIG_WIFI_NRF7001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7001)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)、[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_AP)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_NRF70_DATA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_DATA_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WIFI_NRF7002`、`CONFIG_WIFI_NRF7001`、`CONFIG_NRF70_DATA_TX`。

<a id="CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_DSSS"></a>

## 189.27 `CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_DSSS`

**提示（Prompt）**：2.4 GHz 频段下边缘的直接序列扩频（DSSS）发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_HE"></a>

## 189.28 `CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：2.4 GHz 频段下边缘的高效率（HE）发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_HT"></a>

## 189.29 `CONFIG_NRF70_BAND_2G_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：2.4 GHz 频段下边缘的高吞吐量／甚高吞吐量（HT/VHT）发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:357`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L357)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_DSSS"></a>

## 189.30 `CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_DSSS`

**提示（Prompt）**：2.4 GHz 频段上边缘的 DSSS 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_HE"></a>

## 189.31 `CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：2.4 GHz 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_HT"></a>

## 189.32 `CONFIG_NRF70_BAND_2G_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：2.4 GHz 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_1_LOWER_EDGE_BACKOFF_HE"></a>

## 189.33 `CONFIG_NRF70_BAND_UNII_1_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-1 频段下边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_1_LOWER_EDGE_BACKOFF_HT"></a>

## 189.34 `CONFIG_NRF70_BAND_UNII_1_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-1 频段下边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:382`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L382)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_1_UPPER_EDGE_BACKOFF_HE"></a>

## 189.35 `CONFIG_NRF70_BAND_UNII_1_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-1 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_1_UPPER_EDGE_BACKOFF_HT"></a>

## 189.36 `CONFIG_NRF70_BAND_UNII_1_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-1 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2A_LOWER_EDGE_BACKOFF_HE"></a>

## 189.37 `CONFIG_NRF70_BAND_UNII_2A_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-2A 频段下边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:407`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L407)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2A_LOWER_EDGE_BACKOFF_HT"></a>

## 189.38 `CONFIG_NRF70_BAND_UNII_2A_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-2A 频段下边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L402)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2A_UPPER_EDGE_BACKOFF_HE"></a>

## 189.39 `CONFIG_NRF70_BAND_UNII_2A_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-2A 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L417)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2A_UPPER_EDGE_BACKOFF_HT"></a>

## 189.40 `CONFIG_NRF70_BAND_UNII_2A_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-2A 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2C_LOWER_EDGE_BACKOFF_HE"></a>

## 189.41 `CONFIG_NRF70_BAND_UNII_2C_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-2C 频段下边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2C_LOWER_EDGE_BACKOFF_HT"></a>

## 189.42 `CONFIG_NRF70_BAND_UNII_2C_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-2C 频段下边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2C_UPPER_EDGE_BACKOFF_HE"></a>

## 189.43 `CONFIG_NRF70_BAND_UNII_2C_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-2C 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L437)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_2C_UPPER_EDGE_BACKOFF_HT"></a>

## 189.44 `CONFIG_NRF70_BAND_UNII_2C_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-2C 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L432)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_3_LOWER_EDGE_BACKOFF_HE"></a>

## 189.45 `CONFIG_NRF70_BAND_UNII_3_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-3 频段下边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:447`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L447)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_3_LOWER_EDGE_BACKOFF_HT"></a>

## 189.46 `CONFIG_NRF70_BAND_UNII_3_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-3 频段下边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:442`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L442)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_3_UPPER_EDGE_BACKOFF_HE"></a>

## 189.47 `CONFIG_NRF70_BAND_UNII_3_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-3 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:457`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L457)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_3_UPPER_EDGE_BACKOFF_HT"></a>

## 189.48 `CONFIG_NRF70_BAND_UNII_3_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-3 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_4_LOWER_EDGE_BACKOFF_HE"></a>

## 189.49 `CONFIG_NRF70_BAND_UNII_4_LOWER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-4 频段下边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:467`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L467)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_4_LOWER_EDGE_BACKOFF_HT"></a>

## 189.50 `CONFIG_NRF70_BAND_UNII_4_LOWER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-4 频段下边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:462`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L462)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_4_UPPER_EDGE_BACKOFF_HE"></a>

## 189.51 `CONFIG_NRF70_BAND_UNII_4_UPPER_EDGE_BACKOFF_HE`

**提示（Prompt）**：UNII-4 频段上边缘的 HE 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:477`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L477)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BAND_UNII_4_UPPER_EDGE_BACKOFF_HT"></a>

## 189.52 `CONFIG_NRF70_BAND_UNII_4_UPPER_EDGE_BACKOFF_HT`

**提示（Prompt）**：UNII-4 频段上边缘的 HT/VHT 发射功率回退（Transmit Power Backoff），单位为 dB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L472)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BH_WQ_PRIORITY"></a>

## 189.53 `CONFIG_NRF70_BH_WQ_PRIORITY`

**提示（Prompt）**：处理中断下半部（Bottom Half）的工作队列优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L523)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BH_WQ_STACK_SIZE"></a>

## 189.54 `CONFIG_NRF70_BH_WQ_STACK_SIZE`

**提示（Prompt）**：处理中断下半部（Bottom Half）的工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L531)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_BT_SLOT_TIME"></a>

## 189.55 `CONFIG_NRF70_BT_SLOT_TIME`

**提示（Prompt）**：Wi-Fi 扫描中的蓝牙（BT）时隙分配时间（ms）

**说明（Help）**

连续两次 Wi-Fi 信道扫描之间分配给短距无线（SR）的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SR_COEX && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi 与短距无线（SR）共存支持

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SR_COEX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SR_COEX)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_DEBUG_SHELL"></a>

## 189.56 `CONFIG_NRF70_DEBUG_SHELL`

**提示（Prompt）**：nRF70 驱动调试命令行（Debug Shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_ENABLE_DUAL_VIF"></a>

## 189.57 `CONFIG_NRF70_ENABLE_DUAL_VIF`

**提示（Prompt）**：双虚拟 Wi-Fi 接口（Dual Virtual Wi-Fi Interfaces）

**说明（Help）**

启用两个虚拟 Wi-Fi 接口（Virtual Interfaces，VIF）支持。驱动可同时运行两个 VIF，例如一个接口采用 AP 模式，另一个采用站点（STA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NRF7002 || CONFIG_WIFI_NRF7001) && CONFIG_NET_L2_ETHERNET && CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES = 2
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF7002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7002)、[`CONFIG_WIFI_NRF7001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7001)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_MAX_MANAGED_INTERFACES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WIFI_NRF7002`、`CONFIG_WIFI_NRF7001`。

<a id="CONFIG_NRF70_IRQ_WQ_PRIORITY"></a>

## 189.58 `CONFIG_NRF70_IRQ_WQ_PRIORITY`

**提示（Prompt）**：处理中断请求（IRQ）的工作队列优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
-15
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:519`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L519)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_IRQ_WQ_STACK_SIZE"></a>

## 189.59 `CONFIG_NRF70_IRQ_WQ_STACK_SIZE`

**提示（Prompt）**：处理中断请求（IRQ）的工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:527`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L527)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_LOG_VERBOSE"></a>

## 189.60 `CONFIG_NRF70_LOG_VERBOSE`

原库同名定义共 2 条；本项为数据库第 13648 条记录，各定义分别保留。

**提示（Prompt）**：控制日志信息的详细程度（Verbosity）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_MAX_TX_AGGREGATION"></a>

## 189.61 `CONFIG_NRF70_MAX_TX_AGGREGATION`

**提示（Prompt）**：聚合的最大发送（TX）包数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:490`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L490)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_MAX_TX_PENDING_QLEN"></a>

## 189.62 `CONFIG_NRF70_MAX_TX_PENDING_QLEN`

**提示（Prompt）**：待处理发送（TX）包的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
18
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_MAX_TX_TOKENS"></a>

## 189.63 `CONFIG_NRF70_MAX_TX_TOKENS`

**提示（Prompt）**：发送令牌（TX Token）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[5, 12] if !CONFIG_NRF70_RADIO_TEST
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_RADIO_TEST`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST)。

<a id="CONFIG_NRF70_OFFLOADED_RAW_TX"></a>

## 189.64 `CONFIG_NRF70_OFFLOADED_RAW_TX`

**提示（Prompt）**：nRF70 驱动的卸载式原始发送模式（Offloaded Raw TX Mode）

**说明（Help）**

启用卸载式原始发送模式（Offloaded Raw TX Mode）。此模式可直接发送原始 802.11 帧，跳过常规 Wi-Fi 协议处理。帧构造和发送时序由 Wi-Fi 硬件处理，从而减轻 CPU 负载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF70_OPER_MODES>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_OPER_MODES"></a>

## 189.65 `CONFIG_NRF70_OPER_MODES`

**提示（Prompt）**：nRF70 工作模式（Operating Modes）

**说明（Help）**

选择 nRF70 驱动的工作模式（Operating Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_NRF70_SYSTEM_MODE if !CONFIG_WIFI_USAGE_MODE_SCAN_ONLY
CONFIG_NRF70_SCAN_ONLY
```

**可选项（Choices）**

```text
CONFIG_NRF70_SCAN_ONLY
CONFIG_NRF70_SYSTEM_MODE
CONFIG_NRF70_RADIO_TEST
CONFIG_NRF70_OFFLOADED_RAW_TX
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_USAGE_MODE_SCAN_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_SCAN_ONLY)、[`CONFIG_NRF70_SCAN_ONLY`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SCAN_ONLY)、[`CONFIG_NRF70_RADIO_TEST`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST)、[`CONFIG_NRF70_OFFLOADED_RAW_TX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OFFLOADED_RAW_TX)。

<a id="CONFIG_NRF70_P2P_MODE"></a>

## 189.66 `CONFIG_NRF70_P2P_MODE`

**提示（Prompt）**：驱动中的对等连接（P2P）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)。

<a id="CONFIG_NRF70_PASSIVE_SCAN_ONLY"></a>

## 189.67 `CONFIG_NRF70_PASSIVE_SCAN_ONLY`

**提示（Prompt）**：强制被动扫描（Forced Passive Scan）

**说明（Help）**

强制在所有信道上执行被动扫描（Passive Scan），覆盖应用指定的扫描类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SCAN_ONLY && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:938`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L938)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SCAN_ONLY`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SCAN_ONLY)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_PATCH_DL_CHUNK_SIZE"></a>

## 189.68 `CONFIG_NRF70_PATCH_DL_CHUNK_SIZE`

**提示（Prompt）**：nRF70 固件补丁下载分块大小（字节）

**说明（Help）**

通过 SPI/QSPI 向无线处理单元（RPU）下载 nRF70 固件补丁时，每个数据块的大小。较大的块可减少固件加载所需的总线传输次数；较小的块可降低峰值堆用量。默认值按 SoC 选取，以满足总线 DMA 限制；只有 SoC 的限制比默认设置所考虑的更严格时，才应减小此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048 if CONFIG_SOC_SERIES_NRF54H
4096
```

**取值范围（Ranges）**

```text
[256, 8192]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_SOC_SERIES_NRF54H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)。

<a id="CONFIG_NRF70_PCB_LOSS_2G"></a>

## 189.69 `CONFIG_NRF70_PCB_LOSS_2G`

**提示（Prompt）**：2.4 GHz 频段印制电路板损耗（PCB Loss）

**说明（Help）**

指定天线连接器至射频引脚之间的印制电路板损耗（PCB Loss）。单位为 dB，步进为 1 dB，范围为 0 至 4 dB。仅在接收（RX）路径中计入此损耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_PCB_LOSS_5G_BAND1"></a>

## 189.70 `CONFIG_NRF70_PCB_LOSS_5G_BAND1`

**提示（Prompt）**：5 GHz 频段（5150 MHz 至 5350 MHz，信道 32 至 68）的 PCB 损耗

**说明（Help）**

指定天线连接器至射频引脚之间的印制电路板损耗（PCB Loss）。单位为 dB，步进为 1 dB，范围为 0 至 4 dB。仅在接收（RX）路径中计入此损耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:305`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L305)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_PCB_LOSS_5G_BAND2"></a>

## 189.71 `CONFIG_NRF70_PCB_LOSS_5G_BAND2`

**提示（Prompt）**：5 GHz 频段（5470 MHz 至 5730 MHz，信道 96 至 144）的 PCB 损耗

**说明（Help）**

指定天线连接器至射频引脚之间的印制电路板损耗（PCB Loss）。单位为 dB，步进为 1 dB，范围为 0 至 4 dB。仅在接收（RX）路径中计入此损耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_PCB_LOSS_5G_BAND3"></a>

## 189.72 `CONFIG_NRF70_PCB_LOSS_5G_BAND3`

**提示（Prompt）**：5 GHz 频段（5730 MHz 至 5895 MHz，信道 149 至 177）的 PCB 损耗

**说明（Help）**

指定天线连接器至射频引脚之间的印制电路板损耗（PCB Loss）。单位为 dB，步进为 1 dB，范围为 0 至 4 dB。仅在接收（RX）路径中计入此损耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_PROMISC_DATA_RX"></a>

## 189.73 `CONFIG_NRF70_PROMISC_DATA_RX`

**提示（Prompt）**：驱动中的混杂接收嗅探（Promiscuous RX Sniffer）功能

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_NET_PROMISCUOUS_MODE
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)。

<a id="CONFIG_NRF70_QSPI_LOW_POWER"></a>

## 189.74 `CONFIG_NRF70_QSPI_LOW_POWER`

原库同名定义共 2 条；本项为数据库第 13662 条记录，各定义分别保留。

**提示（Prompt）**：QSPI 低功耗模式（Low Power Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_WIFI_LOW_POWER
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_WIFI_LOW_POWER)。

<a id="CONFIG_NRF70_QSPI_LOW_POWER--record-13663"></a>

## 189.75 `CONFIG_NRF70_QSPI_LOW_POWER`

原库同名定义共 2 条；本项为数据库第 13663 条记录，各定义分别保留。

**提示（Prompt）**：QSPI 低功耗模式（Low Power Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_WIFI_LOW_POWER
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF_WIFI_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_WIFI_LOW_POWER)。

<a id="CONFIG_NRF70_RADIO_TEST"></a>

## 189.76 `CONFIG_NRF70_RADIO_TEST`

**提示（Prompt）**：nRF70 驱动的射频测试模式（Radio Test Mode）

**说明（Help）**

启用 nRF70 驱动的射频测试模式（Radio Test Mode）。此模式用于测试射频（RF）性能和法规符合性，可直接控制无线硬件发送测试图案并测量射频参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF70_OPER_MODES>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_RADIO_TEST_FICR_SHELL"></a>

## 189.77 `CONFIG_NRF70_RADIO_TEST_FICR_SHELL`

**提示（Prompt）**：射频测试 FICR/OTP 编程命令行

**说明（Help）**

注册 `wifi_radio_ficr_prog` 命令集，用于编程 nRF7002 一次性可编程（OTP）存储器。如果应用提供自身集成方式，则禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_RADIO_TEST_SHELL && <choice CONFIG_NRF70_OPER_MODES>
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes） → nRF70 驱动的射频测试模式（Radio Test Mode） → 射频测试命令行命令（Radio Test Shell Commands）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_RADIO_TEST_SHELL`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST_SHELL)、[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_RADIO_TEST_SHELL"></a>

## 189.78 `CONFIG_NRF70_RADIO_TEST_SHELL`

**提示（Prompt）**：射频测试命令行命令（Radio Test Shell Commands）

**说明（Help）**

为 nRF70 射频测试模式注册 `wifi_radio_test` 命令集。需要在应用中自行集成命令行时，可禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_RADIO_TEST && CONFIG_SHELL && <choice CONFIG_NRF70_OPER_MODES>
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes） → nRF70 驱动的射频测试模式（Radio Test Mode）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_RADIO_TEST`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RADIO_TEST)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_RAW_DATA_RX"></a>

## 189.79 `CONFIG_NRF70_RAW_DATA_RX`

**提示（Prompt）**：驱动中的原始接收嗅探（RAW RX Sniffer）功能

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RAW_DATA_TX"></a>

## 189.80 `CONFIG_NRF70_RAW_DATA_TX`

**提示（Prompt）**：驱动中的原始发送（RAW TX）数据通路

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_REG_DOMAIN"></a>

## 189.81 `CONFIG_NRF70_REG_DOMAIN`

**提示（Prompt）**：设备当前所在国家的 ISO/IEC 两字母（Alpha-2）国家代码。默认值为 `00`，表示全球监管域（World Regulatory）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"00"
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RPU_EXTEND_TWT_SP"></a>

## 189.82 `CONFIG_NRF70_RPU_EXTEND_TWT_SP`

**提示（Prompt）**：延长目标唤醒时间（TWT）服务周期（SP）

**说明（Help）**

如果在服务周期（Service Period，SP）开始前接受的帧，未能在 SP 结束前发出，通常会被丢弃，以遵循规范要求的 SP 时间窗口，即不在窗口外发送。此功能在 SP 结束后继续通过标准竞争机制（Contention Mechanism）发送，减少帧丢失。规范允许这种方式，但不推荐。

由于设备在 SP 之后仍主动发送，功耗会增加，增幅取决于 SP 开始时已有的流量。注意，如果某帧是在 SP 开始后提交发送，则会将其排入队列，不使用此机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_LOW_POWER && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_WIFI_LOW_POWER)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RPU_PS_IDLE_TIMEOUT_MS"></a>

## 189.83 `CONFIG_NRF70_RPU_PS_IDLE_TIMEOUT_MS`

**提示（Prompt）**：无线处理单元（RPU）节能空闲超时，单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_WIFI_LOW_POWER && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:555`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L555)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF_WIFI_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_WIFI_LOW_POWER)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RSSI_STALE_TIMEOUT_MS"></a>

## 189.84 `CONFIG_NRF70_RSSI_STALE_TIMEOUT_MS`

**提示（Prompt）**：接收信号强度指示（RSSI）过期超时，单位为毫秒

**说明（Help）**

接收信号强度指示（RSSI）过期超时决定驱动何时向无线处理单元（RPU）重新查询 RSSI。如果存在活动数据流，例如 ping，驱动会从接收帧保存 RSSI 值，并将缓存信息提供给 `wpa_supplicant`。由于缓存值会定期更新，此时适合使用较大的超时值。

如果没有活动数据流，或已超过过期时长，驱动则向 RPU 查询 RSSI 并提供给 `wpa_supplicant`。这种情况下，驱动不保存该值，需要 RPU 提供信息，因此应设置较小的超时值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:606`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L606)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RX_MAX_DATA_SIZE"></a>

## 189.85 `CONFIG_NRF70_RX_MAX_DATA_SIZE`

**提示（Prompt）**：接收（RX）数据最大大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1000 if !CONFIG_NRF70_DATA_TX
1600
```

**取值范围（Ranges）**

```text
[400, 65536]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_DATA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_DATA_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_DATA_TX`。

<a id="CONFIG_NRF70_RX_NUM_BUFS"></a>

## 189.86 `CONFIG_NRF70_RX_NUM_BUFS`

**提示（Prompt）**：接收缓冲区（RX Buffer）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6 if !CONFIG_NRF70_DATA_TX
16
```

**取值范围（Ranges）**

```text
[3, 256]
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:484`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L484)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_DATA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_DATA_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NRF70_DATA_TX`。

<a id="CONFIG_NRF70_RX_WQ_ENABLED"></a>

## 189.87 `CONFIG_NRF70_RX_WQ_ENABLED`

**提示（Prompt）**：接收（RX）工作队列

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:512`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L512)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RX_WQ_PRIORITY"></a>

## 189.88 `CONFIG_NRF70_RX_WQ_PRIORITY`

**提示（Prompt）**：处理接收（RX）的工作队列优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_RX_WQ_ENABLED && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L545)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_RX_WQ_ENABLED`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RX_WQ_ENABLED)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_RX_WQ_STACK_SIZE"></a>

## 189.89 `CONFIG_NRF70_RX_WQ_STACK_SIZE`

**提示（Prompt）**：处理接收（RX）的工作队列栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_RX_WQ_ENABLED && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:549`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L549)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRF70_RX_WQ_ENABLED`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RX_WQ_ENABLED)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_SCAN_ONLY"></a>

## 189.90 `CONFIG_NRF70_SCAN_ONLY`

**提示（Prompt）**：nRF70 仅扫描模式（Scan-only Mode）

**说明（Help）**

启用 nRF70 驱动的仅扫描模式（Scan-only Mode）。此模式仅可执行扫描以发现附近 Wi-Fi 网络，不能建立连接或发送／接收数据，主要用于提高定位准确度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF70_OPER_MODES>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_SR_COEX"></a>

## 189.91 `CONFIG_NRF70_SR_COEX`

**提示（Prompt）**：Wi-Fi 与短距无线（SR）共存支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_SR_COEX_BT_GRANT_ACTIVE_LOW"></a>

## 189.92 `CONFIG_NRF70_SR_COEX_BT_GRANT_ACTIVE_LOW`

**提示（Prompt）**：配置蓝牙授权（BT Grant）为低电平有效

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SR_COEX && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi 与短距无线（SR）共存支持

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SR_COEX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SR_COEX)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_SR_COEX_RF_SWITCH"></a>

## 189.93 `CONFIG_NRF70_SR_COEX_RF_SWITCH`

**提示（Prompt）**：控制短距无线（SR）侧射频开关位置的 GPIO 配置

**说明（Help）**

启用 GPIO 配置，以控制短距无线（SR）侧射频开关的位置。GPIO 为有效状态（1）时，SR 侧射频开关连接到 Wi-Fi 侧，使用共享天线（Shared Antenna）；GPIO 为无效状态（0）时，连接到 SR 侧，使用独立天线（Separate Antenna）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi 与短距无线（SR）共存支持

<a id="CONFIG_NRF70_SR_COEX_SLEEP_CTRL_GPIO_CTRL"></a>

## 189.94 `CONFIG_NRF70_SR_COEX_SLEEP_CTRL_GPIO_CTRL`

**提示（Prompt）**：共存（Coexistence）的 GPIO 控制配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SR_COEX && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi 与短距无线（SR）共存支持

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SR_COEX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SR_COEX)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_SR_COEX_SWCTRL1_OUTPUT"></a>

## 189.95 `CONFIG_NRF70_SR_COEX_SWCTRL1_OUTPUT`

**提示（Prompt）**：将 SWCTRIL1 配置为输出

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF70_SR_COEX && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi 与短距无线（SR）共存支持

**配置项引用（Symbol References）**：[`CONFIG_NRF70_SR_COEX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SR_COEX)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_STA_MODE"></a>

## 189.96 `CONFIG_NRF70_STA_MODE`

**提示（Prompt）**：nRF70 站点（STA）模式

**说明（Help）**

启用 nRF70 驱动的站点（STA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NRF7002 || CONFIG_WIFI_NRF7001) && CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_STA || CONFIG_WIFI_USAGE_MODE_STA_AP
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_NRF70_DATA_TX
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF7002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7002)、[`CONFIG_WIFI_NRF7001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7001)、[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NRF70_DATA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF70_DATA_TX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WIFI_NRF7002`、`CONFIG_WIFI_NRF7001`、`CONFIG_NRF70_DATA_TX`。

<a id="CONFIG_NRF70_SYSTEM_MODE"></a>

## 189.97 `CONFIG_NRF70_SYSTEM_MODE`

**提示（Prompt）**：nRF70 驱动的系统模式（System Mode）

**说明（Help）**

启用 nRF70 驱动的系统模式（System Mode）。这是正常工作模式，支持完整 Wi-Fi 功能，包括 STA、AP 和 P2P 等子模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF70_OPER_MODES>
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → nRF70 工作模式（Operating Modes）

**配置项引用（Symbol References）**：[`CONFIG_NRF70_OPER_MODES`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_OPER_MODES)。

<a id="CONFIG_NRF70_SYSTEM_WITH_RAW_MODES"></a>

## 189.98 `CONFIG_NRF70_SYSTEM_WITH_RAW_MODES`

**提示（Prompt）**：包含原始模式（Raw Modes）的 nRF70 系统模式

**说明（Help）**

启用包含原始模式（Raw Modes）的 nRF70 驱动系统模式（System Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_WIFI_NRF7002 || CONFIG_WIFI_NRF7001) && CONFIG_NRF70_SYSTEM_MODE && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NRF70_RAW_DATA_TX || CONFIG_NRF70_RAW_DATA_RX || CONFIG_NRF70_PROMISC_DATA_RX
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF7002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7002)、[`CONFIG_WIFI_NRF7001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF7001)、[`CONFIG_NRF70_SYSTEM_MODE`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_SYSTEM_MODE)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)、[`CONFIG_NRF70_RAW_DATA_TX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RAW_DATA_TX)、[`CONFIG_NRF70_RAW_DATA_RX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_RAW_DATA_RX)、[`CONFIG_NRF70_PROMISC_DATA_RX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_PROMISC_DATA_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WIFI_NRF7002`、`CONFIG_WIFI_NRF7001`。

<a id="CONFIG_NRF70_TCP_IP_CHECKSUM_OFFLOAD"></a>

## 189.99 `CONFIG_NRF70_TCP_IP_CHECKSUM_OFFLOAD`

**提示（Prompt）**：TCP/IP 校验和卸载（Checksum Offload）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_CHECKSUM_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<a id="CONFIG_NRF70_TX_DONE_WQ_ENABLED"></a>

## 189.100 `CONFIG_NRF70_TX_DONE_WQ_ENABLED`

**提示（Prompt）**：发送完成（TX Done）工作队列，会对性能产生负面影响

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nrf_wifi/Kconfig.nrfwifi:509`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nrf_wifi/Kconfig.nrfwifi#L509)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。

<!-- kconfig-navigation -->

[上一章](P188_drivers_wifi_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P190_drivers_wifi_配置项参考_3.md)
