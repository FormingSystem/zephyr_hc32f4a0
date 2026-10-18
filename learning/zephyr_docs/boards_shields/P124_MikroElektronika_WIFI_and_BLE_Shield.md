---
id: learning.zephyr-docs.boards-shields.page-124
title: MikroElektronika WIFI and BLE Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_wifi_bt_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-wifi-and-ble-shield"></a>

<a id="mikroe-wifi-bt-click"></a>

# 第124章\_MikroElektronika Wi-Fi与BLE扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_wifi_bt_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

扩展板采用Espressif ESP32，将Wi-Fi及Bluetooth任务从主处理器卸载，使用标准mikroBUS UART引脚及Espressif AT命令。也可通过Zephyr调制解调器驱动，将模块配置为原生Wi-Fi网络接口。

![官方原图：MikroE WIFI BLE Click](images/wifi_click.jpg)

<a id="pins-assignment-of-the-shield"></a>

### 扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>RST#，低有效复位</td>
<td>复位引脚，许多板上将其接地，因此应断开</td>
</tr>
<tr>
<td>发送（TX）</td>
<td>UART发送TX通信引脚</td>
</tr>
<tr>
<td>接收（RX）</td>
<td>UART接收RX通信引脚</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板要求开发板配置提供UART接口，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

注意（Note）

部分开发板声明Arduino R3等标准接口，却未定义全部连接；须确认包含完整定义，避免构建错误。

<a id="id2"></a>

<a id="id4"></a>

应烧录Espressif Systems提供的[ESP32 AT Bin](https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Binary_Lists/index.html)软件[注1](#id1)，文中方案命令兼容AT Bin 2.0.0。下载二进制后，将J1接到USB转串口或ESP-Prog等Espressif编程板，安装[ESP-Tool](https://github.com/espressif/esptool) [注2](#id3)并解压文件，进入二进制所在目录后运行以下命令烧录：

```text
esptool.py --chip auto \
--before default_reset \
--after hard_reset write_flash \
--flash_mode dio \
--flash_freq 40m \
--flash_size detect \
0x10000 ota_data_initial.bin \
0x1000 bootloader/bootloader.bin \
0x20000 at_customize.bin \
0x21000 customized_partitions/ble_data.bin \
0x24000 customized_partitions/server_cert.bin \
0x26000 customized_partitions/server_key.bin \
0x28000 customized_partitions/server_ca.bin \
0x2a000 customized_partitions/client_cert.bin \
0x2c000 customized_partitions/client_key.bin \
0x2e000 customized_partitions/client_ca.bin \
0x30000 customized_partitions/factory_param.bin \
0xf000 phy_init_data.bin \
0x100000 esp-at.bin \
0x8000 partitions_at.bin
```

需要时可用--port <Selected PORT>指定端口，用--baud 115200指定波特率。

烧录后可保持连接，以115200、8N1打开终端并复位板卡；应看到启动日志，最后一条显示所烧录AT固件版本。

注意（Note）

若开发板已有网络接口，应阅读网络文档以正确配置两者。为简化示例，可在Networking → Link Layer Options中仅启用Wi-Fi，避免多接口问题。

<a id="build-and-programming"></a>

## 构建与编程（Build and Programming）

调用west build时设置--shield <shield designation>，替换为所需扩展板名称。

以下示例在lpcxpresso55s69上使用mikroBUS串口：

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s69/lpc55s69/cpu0 --shield mikroe_wifi_bt_click_mikrobus samples/net/wifi
west flash
```

以下示例在b_u585i_iot02a开发套件上使用Arduino连接器UART引脚：

```text
# From the root of the zephyr repository
west build -b b_u585i_iot02a --shield mikroe_wifi_bt_click_arduino samples/net/wifi
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Binary_Lists/index.html](https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Binary_Lists/index.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/espressif/esptool](https://github.com/espressif/esptool)

---

[上一章](P123_MikroElektronika_Weather_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P125_nPM1100_EK.md)
