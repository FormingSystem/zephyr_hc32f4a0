---
id: learning.zephyr-docs.boards-shields.page-137
title: NXP M.2 Wi-Fi and BT Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_m2_wifi_bt/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-m-2-wi-fi-and-bt-shield"></a>

<a id="nxp-m2-wifi-bt"></a>

# 第137章\_NXP M.2 Wi-Fi与蓝牙扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_m2_wifi_bt/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此Zephyr扩展板已使用以下M.2模块及硬件测试Wi-Fi与Bluetooth应用：


- Embedded Artist 1XK：采用内含NXP IW416的村田Murata 1XK射频模块
- Embedded Artist 2EL：采用内含NXP IW612的村田Murata 2EL射频模块
- Embedded Artist 2LL：采用内含NXP IW610的村田Murata 2LL射频模块

支持的芯片组、射频模块及M.2模块详情见：


- [NXP IW612芯片组](https://www.nxp.com/products/IW612)
- [NXP IW416芯片组](https://www.nxp.com/products/IW416)
- [NXP IW610芯片组](https://www.nxp.com/products/IW610)
- [村田Murata 2EL射频模块](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2el)
- [村田Murata 1XK射频模块](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1xk)
- [村田Murata 2LL射频模块](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ll)
- [Embedded Artist 1XK模块](https://www.embeddedartists.com/products/1xk-m-2-module)
- [Embedded Artist 2EL模块](https://www.embeddedartists.com/products/2el-m-2-module)
- [Embedded Artist 2LL模块](https://www.embeddedartists.com/products/2ll-m-2-module)

<a id="requirements"></a>

## 前置要求（Requirements）

使用扩展板须满足以下要求：


- M.2模块采用NXP IW416、IW612或IW610，并提供Bluetooth HCI UART及SDIO接口。
- 主机平台有兼容M.2插槽。
- Wi-Fi与Bluetooth共存时，UART驱动须支持控制RTS线，以唤醒睡眠中的蓝牙CPU。
- 默认Bluetooth Shell应用约需490 KB Flash及130 KB RAM。
- 默认Wi-Fi Shell应用约需1 MB Flash及1.2 MB RAM。

<a id="integration-platform"></a>

## 集成平台（Integration Platform）

本扩展板在下列主机平台完成验证与测试；其他平台亦可能使用，但其他组合未持续测试或验证。


- [MIMXRT1060-EVK](../boards_nxp_imx_rt10xx/P007_MIMXRT1060-EVK.md#mimxrt1060_evk) C版。

<a id="fetch-binary-blobs"></a>

## 获取二进制文件（Fetch Binary Blobs）

nxp_m2_wifi_bt运行Bluetooth或Wi-Fi需要二进制固件，使用以下命令取得：

```text
west blobs fetch hal_nxp
```

<a id="programming"></a>

## 编程（Programming）

调用west build时，通过--shield <option>选择以下支持的扩展板：


- nxp_m2_1xk_wifi_bt：采用NXP IW416的Wi-Fi／Bluetooth示例
- nxp_m2_2el_wifi_bt：采用NXP IW612的Wi-Fi／Bluetooth示例
- nxp_m2_2ll_wifi_bt：采用NXP IW610的Wi-Fi／Bluetooth示例

例如：

蓝牙（BT）：

```text
# From the root of the zephyr repository
west build -b mimxrt1060_evk@C//qspi --shield nxp_m2_1xk_wifi_bt samples/bluetooth/classic/handsfree
```

Wi-Fi嵌入式认证客户端（Embedded Supplicant）：

```text
# From the root of the zephyr repository
west build -b mimxrt1060_evk@C//qspi --shield nxp_m2_2ll_wifi_bt samples/net/wifi/shell -- -DEXTRA_CONF_FILE="nxp/overlay_hosted_mcu.conf"
```

Wi-Fi HostAP／WPA认证客户端（Supplicant）：

```text
# From the root of the zephyr repository
west build -b mimxrt1060_evk@C//qspi --shield nxp_m2_2el_wifi_bt samples/net/wifi/shell -- -DEXTRA_CONF_FILE="nxp/overlay_hosted_mcu.conf;nxp/overlay_hostap_hosted_mcu.conf"
```

注意（Note）

构建Wi-Fi应用时，除默认配置外还必须传入nxp/overlay_hosted_mcu.conf，如上述命令所示。

启用HostAP／WPA supplicant还需传入nxp/overlay_hostap_hosted_mcu.conf；上述命令的shield参数可按所选模块更改。

<a id="hardware-rework-to-enable-m-2-interfaces"></a>

## 启用M.2接口的硬件改装（Hardware Rework）

<a id="rework-for-mimxrt1060evk-rev-c"></a>

### MIMXRT1060EVK C版改装

<a id="bluetooth-hci-uart"></a>

#### Bluetooth HCI UART接口


- 焊接R93及R96。
- 移除R193。
- 连接J109，并连接J76第2～3脚。

<a id="i2s-for-bt-sco"></a>

#### Bluetooth SCO音频的I2S接口


- 移除J54及J55，连接J56及J57。
- 移除R220。
- 连接J103。

注意（Note）

J103连接时无法下载Flash，因此下载时应断开，完成后再连接。

<a id="id1"></a>

![官方原图：MIMXRT1060EVK Rev-C BT Rework for M.2](images/mimxrt1060evkc_m2_bt_rework.webp)

MIMXRT1060EVK C版配合M.2模块的Bluetooth改装

## 译注

M.2 Wi-Fi／Bluetooth的内存要求和板级改装均按原文保留；连接J103后无法烧录Flash，烧录时须断开。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [IW416](https://www.nxp.com/products/IW416)：HTTP Error 404: Not Found。
- [IW610](https://www.nxp.com/products/IW610)：HTTP Error 404: Not Found。
- [IW612](https://www.nxp.com/products/IW612)：HTTP Error 404: Not Found。

---

[上一章](P136_NXP_M.2_IEEE_802.15.4_SPI_RCP_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P138_NXP_MX8_DSI_OLED1A_Panel.md)
