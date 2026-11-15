---
id: learning.zephyr-docs.board-samples.page-107
title: ESP_NOW无线通信
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/espnow/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espnow"></a>

# 第107章\_ESP-NOW 无线通信（ESP-NOW）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/espnow/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/espnow/README.rst/..)

<a id="overview"></a>

## 107.1 概述（Overview）

本示例演示在运行 Zephyr 的 Espressif ESP32 开发板上使用 ESP-NOW 点对点（Peer-to-peer）无线协议。无需 Wi-Fi 接入点（Access Point，AP）；两台设备固定在同一信道并直接通信。

设备角色在构建时选择：

> 译注——角色与周期：Kconfig 默认选择 BIDIR，信道默认 1，信标间隔默认 5 秒。BIDIR 的两块板各自发送自己的信标，并非收到一帧后原样回发；发送循环在一次发送后休眠设定秒数，也不是严格的同步时隙。

- BIDIR，双向角色，默认启用：每隔 `CONFIG_ESPNOW_BEACON_INTERVAL_S` 秒发送一个心跳信标（Heartbeat beacon），并打印收到的所有信标。将两块开发板都烧录为该角色，可进行收发回环测试。

- SENDER，发送方：仅运行信标发送线程，忽略接收帧。

- RECEIVER，接收方：仅使用接收回调，不创建信标发送线程。

每个心跳携带序列计数、以毫秒为单位的运行时长，以及发送方的 MAC 地址；线上数据共 14 字节。

> 译注——线上格式：main.c 使用打包结构，seq 与 uptime_ms 各 4 字节，MAC 为 6 字节，共 14 字节；两个整数采用 ESP32 本机小端格式。这里的 14 字节是应用负载，不含无线帧头。接收代码只按长度识别这种结构，没有额外的消息类型或版本字段。

<a id="configuration"></a>

## 107.2 配置（Configuration）

`prj.conf` 中启用以下 Kconfig 选项：

- `CONFIG_WIFI=y`：启用 Espressif Wi-Fi 驱动。即使不使用接入点，ESP-NOW 仍需要该驱动。

- `CONFIG_NETWORKING=y`：必须启用，因为 Wi-Fi 二层驱动在 `subsys/net/Kconfig` 中受 `depends on NETWORKING` 条件约束的范围内选择 `NET_L2_ETHERNET_MGMT`。缺少它时，启动阶段不会注册 Wi-Fi 管理接口，`esp_wifi_start()` 会失败。本示例不使用 Zephyr 网络协议栈本身，只需要 Wi-Fi 驱动接入代码。

构建时通过 `CONFIG_ESPNOW_ROLE_*` 选择角色，见 `Kconfig`。Wi-Fi 信道由 `CONFIG_ESPNOW_CHANNEL` 固定，默认值为 1；无需 AP。

<a id="requirements"></a>

## 107.3 硬件与配置要求（Requirements）

- 两块通过 USB 连接的 ESP32-S3 或 ESP32-C6 DevKit 开发板。

- 两块板必须采用相同的 `CONFIG_ESPNOW_CHANNEL`，默认值为 1。

<a id="building-and-running"></a>

## 107.4 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块、工具链和目标板。网络示例须按本文准备对端、信道与路由器；加密示例须先满足引导程序前提。设备 Shell 命令与主机命令分别执行，日志仅为原文预期输出。本次未构建、烧录、配网、改写密钥或eFuse。

将默认 BIDIR 角色烧录到两块开发板：

> 译注——广播与确认：源码注册全 FF 广播地址，并设置 peer.encrypt=false，本示例不提供加密或对端身份认证。TX OK 是本地发送回调的状态，不等于另一块板的应用已收到；应在接收端核对序列、源 MAC 和长度。发送、接收回调位于 Wi-Fi 任务上下文，扩展回调时不要加入长时间阻塞工作。

```text
west build -b esp32s3_devkitc/esp32s3/procpu samples/boards/espressif/espnow
west flash
```

如需仅构建接收方：

```text
west build -b esp32s3_devkitc/esp32s3/procpu -- -DCONFIG_ESPNOW_ROLE_RECEIVER=y
```

<a id="sample-output"></a>

## 107.5 示例输出（Sample Output）

发送端：

```text
[00:00:00.512,000] <inf> espnow_sample: ESP-NOW v1 ready  ch=1  role=BIDIR
[00:00:00.513,000] <inf> espnow_sample: Beacon thread started  interval=5s
[00:00:05.001,000] <inf> espnow_sample: TX beacon seq=0  uptime=5001 ms  mac=24:d7:eb:55:87:8c
[00:00:05.002,000] <inf> espnow_sample: TX OK  -> ff:ff:ff:ff:ff:ff
```

接收端：

```text
[00:00:05.034,000] <inf> espnow_sample: RX [BCAST] from 24:d7:eb:55:87:8c  rssi=-42  len=14
[00:00:05.034,000] <inf> espnow_sample:   heartbeat seq=0  uptime=5001 ms  src=24:d7:eb:55:87:8c
```

> 译注——源码入口：[src/main.c](../../../samples/boards/espressif/espnow/src/main.c)；[Kconfig](../../../samples/boards/espressif/espnow/Kconfig)。本地源码使用相对链接；上游快照及官方补充说明的摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/boards/espressif/espnow/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/espnow/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/espnow/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或改写密钥与eFuse。

[上一章](P106_低功耗核定时器唤醒.md) · [返回大纲](大纲.md) · [下一章](P108_闪存加密.md)
