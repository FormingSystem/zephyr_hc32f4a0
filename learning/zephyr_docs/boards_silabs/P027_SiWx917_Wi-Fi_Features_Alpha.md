---
id: learning.zephyr-docs.boards-silabs.page-27
title: SiWx917 Wi-Fi Features Alpha
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/siwx917/doc/wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="siwx917-wi-fi-features-alpha"></a>

<a id="siwx917-wifi-features"></a>

# 第27章\_SiWx917 Wi-Fi功能，Alpha阶段

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/radio_boards/siwx917/doc/wifi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

本文概述917 Wi-Fi模块的能力及功能，重点介绍站点（STA）及软件接入点（Soft-AP）模式。

<a id="sta-mode-features"></a>

## 站点模式（STA Mode）功能

917 Wi-Fi模块的站点（Station，STA）模式以客户端身份连接无线网络，主要功能如下：

<a id="scan"></a>

### 扫描（Scan）

STA模式支持网络扫描，以发现可用接入点（Access Point，AP）：

> - 主动扫描（Active Scanning）：主动探测附近网络。
> - 被动扫描（Passive Scanning）：监听信标帧（Beacon Frame）发现网络。
> - 后台扫描（Background Scanning，BG）：不中断当前连接，后台寻找更合适的接入点。

模块每次最多支持11条扫描结果，以便高效发现附近接入点。

SSID过滤只支持指定一个服务集标识符（SSID）。

设备未处于关联状态时执行主动及被动扫描。

设备处于关联状态时执行后台扫描。

若未指定信道，设备扫描全部有效信道。

默认主动扫描驻留时间（Active Dwell Time）为100 ms。

默认被动扫描驻留时间为400 ms。

<a id="security"></a>

### 安全（Security）

模块通过安全机制提供安全可靠连接，支持以下安全模式：

> - 开放（Open）：不加密，适用于无安全保护的网络。
> - Wi-Fi保护访问（Wi-Fi Protected Access，WPA）：相较WEP改进安全性。
> - WPA2：原文称其为多数网络使用的行业标准加密。
> - WPA3：增强加密及对现代威胁的防护。
> - WPA2-SHA256：使用SHA256增强WPA2密码强度。
> - WPA3过渡模式（Transition Mode），WPA2+WPA3：兼容同时使用WPA2及WPA3标准的网络。

这些模式使模块能安全连接多种网络，同时保护数据。

<a id="link-modes"></a>

### 链路模式（Link Modes）

模块支持多种Wi-Fi链路模式，以兼容不同网络：

> - 802.11b：传统模式，最高11 Mbps；原文括注Wi-Fi 0及Wi-Fi 1，保留该非规范代际命名。
> - 802.11g：最高54 Mbps；原文括注Wi-Fi 3，保留该代际命名。
> - 802.11n，即Wi-Fi 4：采用多输入多输出（MIMO）技术实现高吞吐量。
> - 802.11ax，即Wi-Fi 6：提升效率、容量及性能。

<a id="power-save"></a>

### 省电（Power Save）

模块使用省电机制优化能耗。

支持以下传统省电模式：

> - 基于交付流量指示消息（Delivery Traffic Indication Message，DTIM）：利用DTIM间隔，仅在接入点有缓冲数据时唤醒，以降低功耗。
> - 基于监听间隔（Listen Interval）：按定义的间隔周期唤醒检查流量。监听间隔以信标间隔（Beacon Interval）为单位。

设备支持100～1000 ms的省电监听间隔，配置时仍须换算为信标间隔单位。超过1000 ms时按1000 ms处理。基于监听间隔的唤醒在设备连接后生效。若间隔为0，驱动自动改用DTIM唤醒。若固件曾禁用省电，重新启用时驱动使用此前配置的监听间隔。

该省电监听间隔必须小于关联或重新关联请求帧中通告的监听间隔。

还支持以下缓冲数据包获取方式：

> - 省电轮询（Power Save Polling，PS-Poll）：设备进入省电模式后，从接入点获取缓冲数据包。
> - 服务质量空数据帧（QoS Null Data）：设备发送QoS Null帧，以节能方式获取接入点的缓冲数据包。

设备默认启用专有Enhanced Max PSP模式获取缓冲数据包，以改善性能。

若通过关闭CONFIG_WIFI_SILABS_SIWX91X_ENHANCED_MAX_PSP禁用该功能，则启用QoS Null帧。QoS Null与Enhanced Max PSP互斥。

断开连接后省电被禁用，如新连接仍需省电，须重新启用。

监测间隔（Monitor Interval）从最近收到的非ACK数据包开始计时；期间若没有收到数据包，设备进入睡眠。配置为0时使用默认50 ms。此参数用于QoS Null Data或Enhanced Max PSP，设备支持的最大值为1000 ms。

设备当前不支持timeout_ms。

<a id="management-frame-protection"></a>

### 管理帧保护（Management Frame Protection，MFP）

支持802.11w以保护管理帧，防御：

> - 解除认证攻击（Deauthentication Attack）。
> - 解除关联攻击（Disassociation Attack）。

默认启用802.11w。

不同安全模式的推荐MFP值：

> <table>
> <tr>
> <th>安全模式（Security Mode）</th>
> <th>禁用MFP</th>
> <th>支持MFP，可选</th>
> <th>要求MFP，必需</th>
> </tr>
> <tr>
> <td>开路（Open）</td>
> <td>是（Yes）</td>
> <td></td>
> <td></td>
> </tr>
> <tr>
> <td>WPA</td>
> <td>是（Yes）</td>
> <td></td>
> <td></td>
> </tr>
> <tr>
> <td>WPA + WPA2</td>
> <td></td>
> <td>是（Yes）</td>
> <td>可选（Optional）</td>
> </tr>
> <tr>
> <td>WPA2</td>
> <td></td>
> <td>是（Yes）</td>
> <td>可选（Optional）</td>
> </tr>
> <tr>
> <td>WPA2 + WPA3</td>
> <td></td>
> <td>是（Yes）</td>
> <td>否（No）</td>
> </tr>
> <tr>
> <td>WPA3</td>
> <td></td>
> <td>是（Yes）</td>
> <td>是（Yes）</td>
> </tr>
> </table>

<a id="bg-scan-and-roaming"></a>

### 后台扫描与漫游（BG Scan and Roaming）

漫游使Wi-Fi站点在同一网络的不同接入点之间无缝切换而不丢失连接，从而在跨越AP覆盖区域时保持连接。

设备支持传统漫游（Legacy Roaming），包含以下过程：

> 1. 后台扫描（BG Scan）：
>
>
>   - 在STA保持网络连接时执行标准扫描。
>   - 接收信号强度指示（Received Signal Strength Indicator，RSSI）低于预设阈值时触发。
> 2. 漫游（Roaming）：
>
>
>   - RSSI跨过阈值且满足漫游迟滞（Roaming Hysteresis）条件时启动。
>   - 漫游过程可使用空数据包（Null Data Packet，NDP）或解除认证帧，默认使用NDP。可通过CONFIG_WIFI_SILABS_SIWX91X_ROAMING_USE_DEAUTH选择解除认证帧。

限制与问题（Challenges）：

> - Zephyr当前没有传统漫游API。虽然已定义802.11r漫游API，但它不适用于传统漫游。

当前设计：

> - 后台扫描通过Scan API执行；此时忽略Scan API的channel参数，使用首次前台扫描得到的信道。
> - 漫游配置在第一次后台扫描时完成，参数通过Kconfig选项管理。

默认启用漫游，但须执行后台扫描以初始化及配置漫游参数。关闭WIFI_SILABS_SIWX91X_ENABLE_ROAMING可禁用漫游。

STA断开后后台扫描停止，需要再次发出后台扫描命令，以启用后台扫描及漫游。

设备支持后台扫描中的多重探测（Multi-probe），也可扫描不同SSID的AP，此配置可通过Kconfig禁用。

<a id="target-wake-time-twt"></a>

### 目标唤醒时间（Target Wake Time，TWT）

模块支持符合Wi-Fi 6标准的个体TWT（Individual TWT）：

> - 个体TWT允许模块与AP协商唤醒时间，优化功耗；模块只支持作为请求方（Requester）。
> - 不支持广播TWT（Broadcast TWT）。

此功能适用于要求低能耗及周期连接的IoT设备。

设备不支持显式TWT（Explicit TWT），也不支持TWT信息元素（Information Element）。

设备不支持TWT快速设置，不能配置TWT间隔、提前唤醒时长及对话令牌（Dialog Token）等参数。

<a id="bugs-and-limitations"></a>

### 缺陷与限制（Bugs and Limitations）

> - WPA3的同时等值认证（SAE）密码最多64个字符。
> - 不支持可扩展认证协议（EAP）安全模式。
> - 设备仅支持20 MHz带宽及1条空间流。
> - 不支持802.11r。
> - 不支持Wi-Fi多媒体（WMM）省电模式。
> - Wi-Fi状态wifi_iface_status中的twt_capable可能为true，即使AP不支持TWT；当连接使用802.11ax但AP禁用TWT时会出现这种情况。

<a id="soft-ap-mode-features"></a>

## 软件接入点（Soft-AP）模式功能

在软件接入点（Software Access Point，Soft-AP）模式下，917 Wi-Fi模块可作为AP供其他设备连接，主要功能如下：

<a id="id1"></a>

### 安全（Security）

模块为连接Soft-AP的设备提供安全连接，支持以下安全模式：

> - 开放（Open）：不加密，适用于无安全保护的网络。
> - Wi-Fi保护访问（Wi-Fi Protected Access，WPA）：相较WEP改进安全性。
> - WPA2：原文称其为多数网络使用的行业标准加密。
> - 混合模式（Mixed Mode），WPA+WPA2：兼容同时使用WPA及WPA2标准的网络。

这些模式支持灵活配置连接Soft-AP的设备。

<a id="id2"></a>

### 链路模式（Link Modes）

Soft-AP支持以下链路模式：

> - 802.11b：用于基本连接的传统模式；原文括注Wi-Fi 0及Wi-Fi 1。
> - 802.11g：为较新设备提升速率；原文括注Wi-Fi 3。
> - 802.11n，即Wi-Fi 4：为高要求应用提供高速连接。

<a id="hidden-ssid"></a>

### 隐藏SSID（Hidden SSID）

允许在广播中隐藏网络名称SSID；原文将避免向未授权用户显示SSID描述为隐私增强。

<a id="id3"></a>

### 缺陷与限制（Bugs and Limitations）

> - 设备仅支持20 MHz带宽及1条空间流。
> - STA与BLE可同时共存，但AP与BLE不能同时运行。

<a id="common-features"></a>

## 通用功能（Common Features）

<a id="regulatory-domain"></a>

### 监管域（Regulatory Domain）

SiWx91x驱动支持监管域配置，在STA及Soft-AP模式下执行各区域的信道与发射功率限制。

> - 国家代码采用ISO/IEC 3166-1二字母代码（Alpha-2），例如US、IN、FR。
> - 驱动将支持的国家代码映射为SiWx91x固件区域标识。
> - 支持区域包括EU、CN、KR、JP及US。
> - 驱动默认应用US监管域。

注意（Note）

必须在扫描、连接或启动Soft-AP等设备激活操作前配置监管域，以确保仅使用允许的信道及发射功率。

请求的国家代码不受支持时，驱动回退到默认US域。

<a id="maximum-transmit-power"></a>

### 最大发射功率（Maximum Transmit Power）

驱动在STA及Soft-AP模式下均支持配置最大发射（TX）功率，该值是射频输出上限，仍受硬件及监管约束。

> - 通过设备树（Devicetree）属性配置。
> - 未指定时，默认最大TX功率为31 dBm。

<a id="device-tree-properties"></a>

#### 设备树属性（Devicetree Properties）

> - wifi-max-tx-pwr-scan：Wi-Fi扫描期间的最大TX功率，单位dBm，仅适用于STA模式。
> - wifi-max-tx-pwr-join：加入Wi-Fi网络时的最大TX功率，单位dBm。

注意（Note）

SiWx91x固件不支持按速率分别控制TX功率。

<a id="rts-threshold"></a>

### 请求发送阈值（RTS Threshold）

驱动支持配置请求发送（Request to Send，RTS）阈值：帧大小超过该值时启用RTS／CTS握手。

> - 有效范围：0～2347字节。
> - 设为0表示每个发送帧之前都先发送RTS帧。
> - 默认RTS阈值为2346字节。

## 译注

本页为官方Alpha阶段Wi-Fi功能说明。扫描、节能、漫游、目标唤醒时间（TWT）、Soft-AP及法规限制分别保留；原文将802.11b称为Wi-Fi 0与1、将802.11g称为Wi-Fi 3，这些称呼不是通用的正式代际命名。

---

[上一章](P026_SiWx917_Wi-Fi_6_and_Bluetooth_LE_8_MB_Flash_8_MB_ext_PSRAM_Radio_Board_SiWx91x-RB4342A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P028_SixG301_10_dBm_4_MB_Flash_Radio_Board.md)
