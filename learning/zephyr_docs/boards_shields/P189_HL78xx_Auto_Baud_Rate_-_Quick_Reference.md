---
id: learning.zephyr-docs.boards-shields.page-189
title: HL78xx Auto Baud Rate - Quick Reference
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/auto_baudrate/hl78xx_auto_baudrate_quick_reference.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="hl78xx-auto-baud-rate-quick-reference"></a>

<a id="hl78xx-auto-baudrate-quick-reference"></a>

# 第189章\_HL78xx自动波特率速查（Auto Baud Rate - Quick Reference）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/swir_hl78xx_ev_kit/doc/auto_baudrate/hl78xx_auto_baudrate_quick_reference.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="enable-feature"></a>

## 启用功能

```text
# In prj.conf
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y  # Your target rate
```

<a id="common-configurations"></a>

## 常用配置（Common Configurations）

<a id="preset-1-smart-default-recommended"></a>

### 预设1：智能默认配置，推荐

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="921600,9600,57600,38400,115200"
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=4
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=3
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=y
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```


- 适用场景：通用用途，已知或未知波特率。
- 对启动时间的影响：已在目标速率时约50～100 ms；需要检测时约4～20秒。
- 智能之处：仅在初始通信失败时才进行完整检测。

<a id="preset-2-ultra-fast-boot-known-rate"></a>

### 预设2：超快启动，速率已知

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="921600"
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=1
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=1
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```


- 适用场景：已知调制解调器处于目标速率。
- 对启动时间的影响：约50～100 ms。
- 警告：调制解调器波特率不一致时将失败。

<a id="preset-3-high-speed"></a>

### 预设3：高速

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="921600,460800,230400,115200"
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=3
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=3
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=y
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```


- 适用场景：需要高吞吐量。
- 对启动时间的影响：最佳约50 ms，最差约3～12秒。
- 注意：确认UART硬件支持高波特率。

<a id="preset-4-robust-production"></a>

### 预设4：可靠量产配置

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_DETECTION_BAUDRATES="115200,57600,38400,19200,9600,921600"
CONFIG_MODEM_HL78XX_AUTOBAUD_TIMEOUT=8
CONFIG_MODEM_HL78XX_AUTOBAUD_RETRY_COUNT=5
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=y
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```


- 适用场景：现场部署，要求最高可靠性。
- 对启动时间的影响：最佳约50 ms，最差约40秒。
- 特性：诊断回退及全面检测。

<a id="preset-5-testing-development-non-persistent"></a>

### 预设5：测试／开发，不持久保存

```text
CONFIG_MODEM_HL78XX_AUTO_BAUDRATE=y
CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600=y
CONFIG_MODEM_HL78XX_AUTOBAUD_CHANGE_PERSISTENT=n
CONFIG_MODEM_HL78XX_AUTOBAUD_START_WITH_TARGET_BAUDRATE=y
CONFIG_MODEM_HL78XX_AUTOBAUD_ONLY_IF_COMMS_FAIL=y
```


- 适用场景：临时测试。
- 注意：断电重启后，调制解调器恢复先前波特率。

<a id="supported-baud-rates"></a>

## 支持的波特率（Supported Baud Rates）

<table>
<tr>
<th>速率（Rate）</th>
<th>Kconfig选项</th>
<th>使用场景</th>
</tr>
<tr>
<td>9600</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_9600</code></td>
<td>旧版接口（Legacy）</td>
</tr>
<tr>
<td>19200</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_19200</code></td>
<td>旧版接口（Legacy）</td>
</tr>
<tr>
<td>38400</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_38400</code></td>
<td>标准模式（Standard）</td>
</tr>
<tr>
<td>57600</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_57600</code></td>
<td>标准模式（Standard）</td>
</tr>
<tr>
<td>115200</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_115200</code></td>
<td>默认值，推荐</td>
</tr>
<tr>
<td>230400</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_230400</code></td>
<td>高速</td>
</tr>
<tr>
<td>460800</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_460800</code></td>
<td>高速</td>
</tr>
<tr>
<td>921600</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_921600</code></td>
<td>超高速</td>
</tr>
<tr>
<td>3000000</td>
<td><code>CONFIG_MODEM_HL78XX_TARGET_BAUDRATE_3000000</code></td>
<td>最高速率，仅HL7812</td>
</tr>
</table>

<a id="state-flow"></a>

## 状态流程（State Flow）

```text
Power ON
    ↓
[START_WITH_TARGET=y?] → Try target first → [AUTOBAUD_AT_BOOT=y?]
    ↓                                        ↓
Wait KSUP → [ONLY_IF_COMMS_FAIL=y?] → Try Target
    ↓                                        ↓
Post-Restart → Communication Success? → Skip Detection
    ↓                     ↓
    |              Communication Fails
    |                     ↓
    +----------→ Detect Baud Rate
                          ↓
                  Rate Detected?
                          ↓
                 Switch to Target (AT+IPR)
                          ↓
              [CHANGE_PERSISTENT=y?] → AT&W
                          ↓
                  Initialize Modem
```

<a id="log-messages"></a>

## 日志消息（Log Messages）

<a id="success-smart-default"></a>

### 成功：智能默认配置

```text
[hl78xx] Checking if modem is ready at target baud rate 921600...
[hl78xx] Modem ready at target rate, skipping detection
[hl78xx] Baud rate switch not needed
```

<a id="detection-triggered"></a>

### 触发检测

```text
[hl78xx] Modem not responding at target rate 921600, starting detection...
[hl78xx] Trying baud rate: 9600
[hl78xx] Modem responded at 9600 baud
[hl78xx] Saving persistent baud rate with AT&W...
```

<a id="non-persistent-mode"></a>

### 非持久化模式（Non-Persistent Mode）

```text
[hl78xx] Switching baud rate from 9600 to 921600
[hl78xx] Non-persistent mode: skipping AT&W
```

<a id="failure"></a>

### 失败（Failure）

```text
[hl78xx] Failed to detect modem baud rate
[hl78xx] Retrying baud rate detection (attempt 2/3)
```

<a id="troubleshooting"></a>

## 故障排查（Troubleshooting）

<table>
<tr>
<th>现象（Symptom）</th>
<th>可能原因</th>
<th>解决方法（Solution）</th>
</tr>
<tr>
<td>无法检测调制解调器波特率</td>
<td>检测列表缺少该速率</td>
<td>向检测列表添加速率</td>
</tr>
<tr>
<td>每种速率都超时</td>
<td>调制解调器未就绪</td>
<td>增加超时时间。</td>
</tr>
<tr>
<td>卡在AT&amp;W</td>
<td>UART配置不匹配</td>
<td>修复：先重新配置UART</td>
</tr>
<tr>
<td>速率未持久保存</td>
<td>持久化被禁用</td>
<td>启用CHANGE_PERSISTENT</td>
</tr>
</table>

<a id="at-commands-reference"></a>

## AT命令参考（AT Commands Reference）

```text
AT+IPR?
AT+IPR=115200
AT&W
```

<a id="api-functions-internal"></a>

## API函数，内部使用

```text
int hl78xx_try_baudrate(struct hl78xx_data *data, uint32_t baudrate);
int hl78xx_detect_current_baudrate(struct hl78xx_data *data);
int hl78xx_switch_baudrate(struct hl78xx_data *data, uint32_t target_baudrate);
```

<a id="performance-tips"></a>

## 性能建议（Performance Tips）


1. 启用智能标志以获得最快启动。
2. 按可能性排列检测列表。
3. 已知环境中使用较短超时。
4. 启用持久化，避免重新检测。
5. 仅在时序受控时使用AUTOBAUD_AT_BOOT。

<a id="compatibility"></a>

## 兼容性（Compatibility）


- HL7812／HL7800
- Zephyr 4.4及更高版本
- 所有受支持开发板
- 智能检测将启动时间从约20秒缩短到约50～100 ms。

<a id="license"></a>

## 许可证（License）

版权Copyright (c) 2025 Netfeasa Ltd.

SPDX许可证标识：Apache-2.0


---

最后更新：2025-12-06

---

[上一章](P188_HL78xx_Auto_Baud_Rate_Switching.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P190_HL_RC_Module_Evaluation_Kit_Shield.md)
