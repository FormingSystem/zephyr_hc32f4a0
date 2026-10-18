---
id: learning.zephyr-docs.boards-shields.page-188
title: HL78xx Auto Baud Rate Switching
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/auto_baudrate/hl78xx_auto_baudrate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="hl78xx-auto-baud-rate-switching"></a>

<a id="hl78xx-auto-baudrate"></a>

# 第188章\_HL78xx自动波特率切换（Auto Baud Rate Switching）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/auto_baudrate/hl78xx_auto_baudrate.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此功能为Sierra Wireless HL78xx调制解调器驱动提供自动波特率检测与切换。驱动可自动检测调制解调器当前波特率，并用AT+IPR命令切换到配置的目标波特率。

<a id="features"></a>

## 功能（Features）


- 自动检测：依次尝试常用波特率列表，检测调制解调器当前速率。
- 动态切换：用AT+IPR命令将调制解调器波特率改为配置的目标值。
- 可配置：支持9600～921600 bps的多种波特率。
- 重试机制：重试次数可配置，提高检测可靠性。
- 状态机集成：集成到调制解调器初始化序列。

<a id="configuration"></a>

## 配置（Configuration）

在项目prj.conf中启用该功能：

```text
# Enable auto baud rate detection and switching
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y

# Set target baud rate (default is 115200)
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y

# Configure detection baud rates (comma-separated list)
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="115200,9600,57600,38400,19200"

# Set timeout for each detection attempt (in seconds)
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=4

# Set number of retries
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=3

# Save baud rate change to modem NVMEM (default: y, recommended)
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=y

# Try target baud rate first before detection list (default: y, faster)
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y

# Only perform auto-baud if initial communication fails (default: y, efficient)
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y

# Perform auto-baud immediately at boot, skip KSUP wait (default: n)
CONFIG_MODEM_HL78XX_AUTOBAUD_AT_BOOT=n
```

<a id="supported-baud-rates"></a>

## 支持的波特率（Supported Baud Rates）

支持以下波特率：


- 9600 bps
- 19200 bps
- 38400 bps
- 57600 bps
- 115200 bps，默认值
- 230400 bps
- 460800 bps
- 921600 bps
- 3000000 bps，仅HL7812

<a id="how-it-works"></a>

## 工作过程（How It Works）

<a id="detection-phase-modem-hl78xx-state-set-baudrate"></a>

### 检测阶段：MODEM_HL78XX_STATE_SET_BAUDRATE

上电后，调制解调器进入SET_BAUDRATE状态时：


1. 驱动依次尝试检测列表中的波特率。
2. 对每个速率执行：


  - 将UART配置到该波特率。
  - 发送AT命令。
  - 等待OK响应。
3. 收到响应后，即确定当前波特率。

<a id="switching-phase"></a>

### 切换阶段（Switching Phase）

如果检测出的波特率与目标不同：


1. 以当前波特率发送AT+IPR=<target_baudrate>。
2. 等待OK响应。
3. 等待2.5秒，让调制解调器应用更改。
4. 将主机UART重新配置为新波特率。
5. 等待50 ms，使UART稳定。
6. 发送AT测试命令，验证通信。
7. 发送AT&W，将配置保存到非易失性存储器NVMEM。

注意（Note）

波特率切换完成后，状态机运行重启后脚本，等待KUSP主动上报结果码（URC），再继续初始化。

<a id="state-transitions"></a>

### 状态转换（State Transitions）

```text
AWAIT_POWER_ON --> SET_BAUDRATE --> RUN_INIT_SCRIPT
                        |
                        +--> [On Failure] --> RUN_INIT_FAIL_DIAGNOSTIC_SCRIPT
```

<a id="use-cases"></a>

## 使用场景（Use Cases）

<a id="use-case-1-unknown-modem-baud-rate"></a>

### 场景1：调制解调器波特率未知

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="115200,9600,57600,38400,19200"
```

<a id="use-case-2-high-speed-communication"></a>

### 场景2：高速通信

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
```

<a id="use-case-3-fast-boot-with-known-baud-rate"></a>

### 场景3：已知波特率时快速启动

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=2
```

结果：如果调制解调器已处于目标速率，启动时间约50～100 ms。

<a id="use-case-4-production-field-deployment"></a>

### 场景4：量产／现场部署

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="115200,57600,38400,19200,9600"
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=8
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=5
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=y
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```

<a id="use-case-5-temporary-baud-rate-change"></a>

### 场景5：临时更改波特率

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=n
```

注意（Note）

断电重启或AT+CFUN复位后，调制解调器将恢复先前波特率。

<a id="at-commands-used"></a>

## 使用的AT命令（AT Commands Used）

<a id="query-current-baud-rate"></a>

### 查询当前波特率

```text
AT+IPR?
```

响应（Response）：

```text
+IPR: <rate>
+IPR: 0
```

<a id="set-fixed-baud-rate"></a>

### 设置固定波特率

```text
AT+IPR=<rate>
```

其中<rate>可以是：


- 9600
- 19200
- 38400
- 57600
- 115200
- 230400
- 460800
- 921600
- 3000000，仅HL7812

重要提示（Important）

新波特率约2秒后生效。使用AT&W可使配置在断电重启后仍然保留。

<a id="troubleshooting"></a>

## 故障排查（Troubleshooting）

<a id="detection-fails"></a>

### 检测失败（Detection Fails）

现象：多次重试后调制解调器进入诊断状态。

解决方法（Solutions）：


1. 确认检测列表包含调制解调器当前波特率。
2. 增加超时时间。
3. 检查UART接线及信号质量。
4. 确认调制解调器已供电且能响应。

<a id="switching-fails"></a>

### 切换失败（Switching Fails）

现象：检测成功，但切换失败。

解决方法（Solutions）：


1. 确认调制解调器及UART均支持目标波特率。
2. 检查UART时钟限制。
3. 尝试较低波特率。
4. 确认固件支持AT+IPR。

<a id="communication-lost-after-switch"></a>

### 切换后通信丢失（Communication Lost After Switch）

根因：发送AT&W前未重新配置主机UART。

解决方法（Solutions）：


1. 在AT&W之前重新配置主机UART。
2. 发送AT+IPR后等待2.5秒。
3. 等待KUSP URC。
4. 检查UART缓冲及流控。

<a id="disabling-auto-baud-causes-failure"></a>

### 禁用自动波特率后失败

根因：调制解调器保持已保存波特率，但UART默认值不同。

解决方法（Solutions）：


- 保持自动波特率功能启用，推荐。
- 更新设备树UART速率：

```text
&uart_modem {
    current-speed = <921600>;
};
```


- 禁用自动波特率前，手动复位调制解调器波特率。

<a id="implementation-details"></a>

## 实现细节（Implementation Details）

<a id="key-functions"></a>

### 关键函数（Key Functions）

```text
static int hl78xx_try_baudrate(struct hl78xx_data *data, uint32_t baudrate);
static int hl78xx_detect_current_baudrate(struct hl78xx_data *data);
static int hl78xx_switch_baudrate(struct hl78xx_data *data, uint32_t target_baudrate);
```

<a id="state-handler"></a>

### 状态处理函数（State Handler）

```text
static int hl78xx_on_set_baudrate_state_enter(struct hl78xx_data *data);
static void hl78xx_set_baudrate_event_handler(struct hl78xx_data *data,
                                              enum hl78xx_event evt);
```

<a id="data-structure"></a>

### 数据结构（Data Structure）

```text
struct uart_status {
#ifdef CONFIG_MODEM_HL78XX_AUTO_BAUDRATE
    uint32_t current_baudrate;
    uint32_t target_baudrate;
    uint8_t baudrate_detection_retry;
#endif
};
```

<a id="license"></a>

## 许可证（License）

版权Copyright (c) 2025 Netfeasa Ltd.

SPDX许可证标识：Apache-2.0


---

最后更新：2025-12-06

## 译注

自动波特率、固定目标值及持久保存是不同选项。AT+IPR后须等待并先重配主机UART，再发送AT&W。

---

[上一章](P187_ST_STM32F4DIS-CAM.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P189_HL78xx_Auto_Baud_Rate_-_Quick_Reference.md)
