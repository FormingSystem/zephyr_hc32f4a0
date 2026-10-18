---
id: learning.zephyr-docs.boards-shields.page-136
title: NXP M.2 IEEE 802.15.4 SPI RCP Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_m2_ieee802154/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-m-2-ieee-802-15-4-spi-rcp-shield"></a>

<a id="nxp-m2-ieee802154"></a>

# 第136章\_NXP M.2 IEEE 802.15.4 SPI无线协处理器扩展板（RCP Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_m2_ieee802154/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

该Zephyr扩展板通过主机M.2插槽上的NXP模块，提供SPI传输的IEEE 802.15.4无线协处理器（RCP）。RCP处理802.15.4射频，通过采用HDLC帧的SPI链路spi,hdlc-rcp-if承载Spinel协议与主机通信；适用于OpenThread边界路由器等应用，由主机运行OpenThread协议栈，M.2模块提供射频。

已测试以下M.2模块：


- Embedded Artist 2EL：采用内含NXP IW612的村田Murata 2EL射频模块
- Embedded Artist 2LL：采用内含NXP IW610的村田Murata 2LL射频模块

支持的芯片组、射频模块及M.2模块详情见：


- [NXP IW612芯片组](https://www.nxp.com/products/IW612)
- [NXP IW610芯片组](https://www.nxp.com/products/IW610)
- [村田Murata 2EL射频模块](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2el)
- [村田Murata 2LL射频模块](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2ll)
- [Embedded Artist 2EL模块](https://www.embeddedartists.com/products/2el-m-2-module)
- [Embedded Artist 2LL模块](https://www.embeddedartists.com/products/2ll-m-2-module)

<a id="requirements"></a>

## 前置要求（Requirements）

使用扩展板须满足以下要求：


- 提供SPI RCP接口并采用NXP IW612或IW610的M.2模块。
- 主机平台须有兼容M.2插槽及空闲SPI控制器，提供SCK、SDI、SDO、片选GPIO及中断GPIO。
- 板级覆盖文件须启用主机SPI控制器，例如MIMXRT1060-EVK C版的&lpspi4，配置cs-gpios及pinctrl，并创建带int-gpios的spi,hdlc-rcp-if设备节点。

<a id="integration-platform"></a>

## 集成平台（Integration Platform）

本扩展板在下列主机平台完成验证与测试；其他平台亦可能使用，但其他组合未持续测试或验证。


- [MIMXRT1060-EVK](../boards_nxp_imx_rt10xx/P007_MIMXRT1060-EVK.md#mimxrt1060_evk) C版，目标mimxrt1060_evk@C/mimxrt1062/qspi。

<a id="fetch-binary-blobs"></a>

## 获取二进制文件（Fetch Binary Blobs）

M.2模块需要二进制固件，使用以下命令取得：

```text
west blobs fetch hal_nxp
```

<a id="programming"></a>

## 编程（Programming）

调用west build时，以--shield <option>指定以下名称。


- nxp_m2_2el_2ll_ieee802154：用于采用IW612村田2EL或IW610村田2LL模块的IEEE 802.15.4 SPI RCP。

同一个扩展板定义支持两种M.2模块：


- IW612村田2EL模块
- IW610村田2LL模块

通过命令行配置片段选择模块：IW612使用mimxrt1060_evkc_iw612.conf，IW610使用mimxrt1060_evkc_iw610.conf。两种模块的覆盖文件及引脚分配相同。

OpenThread边界路由器是Wi-Fi与Thread组合应用，将nxp_m2_2ll_wifi_bt Wi-Fi／蓝牙扩展板与nxp_m2_2el_2ll_ieee802154 RCP扩展板一起使用，并需要RCP主机覆盖配置、板级及模块级配置片段。

为MIMXRT1060-EVK C版及IW612村田2EL模块构建：

```text
west build -p -b mimxrt1060_evk@C/mimxrt1062/qspi \
    -d build_mimxrt1060_evk/border_router_iw612 \
    --shield "nxp_m2_2ll_wifi_bt nxp_m2_2el_2ll_ieee802154" \
    zephyr/samples/net/openthread/border_router \
    -- -DEXTRA_CONF_FILE="overlay-ot-rcp-host-wifi-nxp.conf \
    boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evk_mimxrt1062_qspi_C.conf \
    boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evkc_iw612.conf"
```

使用IW610村田2LL模块时，改用IW610配置片段：

```text
west build -p -b mimxrt1060_evk@C/mimxrt1062/qspi \
    -d build_mimxrt1060_evk/border_router_iw610 \
    --shield "nxp_m2_2ll_wifi_bt nxp_m2_2el_2ll_ieee802154" \
    zephyr/samples/net/openthread/border_router \
    -- -DEXTRA_CONF_FILE="overlay-ot-rcp-host-wifi-nxp.conf \
    boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evk_mimxrt1062_qspi_C.conf \
    boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evkc_iw610.conf"
```

EXTRA_CONF_FILE中的配置片段依次应用：


- overlay-ot-rcp-host-wifi-nxp.conf：基础OpenThread RCP主机及NXP Wi-Fi配置，最初针对RW610调整。
- boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evk_mimxrt1062_qspi_C.conf：RT1060 EVKC的M.2 IW612／IW610 RCP覆盖设置，禁用RW610专有选项，调整堆与网络缓冲区并设置日志。
- boards/mimxrt1060_evk_mimxrt1062_qspi_C/mimxrt1060_evkc_iw612.conf或mimxrt1060_evkc_iw610.conf：分别选择IW612或IW610的模块专用设置。

注意（Note）

扩展板默认选择HDLC RCP SPI接口并启用OpenThread L2。主机SPI引脚复用及GPIO由boards/<board>.overlay提供。

<a id="pin-assignments-mimxrt1060-evk-rev-c"></a>

## MIMXRT1060-EVK C版引脚分配

该平台的RCP链路使用LPSPI4，信号如下：

<table>
<tr>
<th>信号（Signal）</th>
<th>引脚（Pin）</th>
<th>备注（Notes）</th>
</tr>
<tr>
<td>SPI串行数据输入SDI</td>
<td>GPIO_B0_01</td>
<td>LPSPI4串行数据输入SDI</td>
</tr>
<tr>
<td>SPI串行数据输出SDO</td>
<td>GPIO_B0_02</td>
<td>LPSPI4串行数据输出SDO</td>
</tr>
<tr>
<td>SPI串行时钟（SCK）</td>
<td>GPIO_B0_03</td>
<td>LPSPI4串行时钟SCK</td>
</tr>
<tr>
<td>SPI片选（CS）</td>
<td>GPIO_B0_00，对应GPIO2.00</td>
<td>低有效片选</td>
</tr>
<tr>
<td>SPI中断INT</td>
<td>GPIO_B0_04，对应GPIO2.04</td>
<td>RCP主机中断，低有效</td>
</tr>
</table>

注意（Note）

板级覆盖文件禁用LCD接口&lcdif，释放LPSPI4所需GPIO_B0_xx引脚。

## 译注

M.2 IEEE 802.15.4采用SPI承载HDLC／Spinel RCP。模块固件、主机引脚及配置片段顺序须配套。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [IW610](https://www.nxp.com/products/IW610)：HTTP Error 404: Not Found。
- [IW612](https://www.nxp.com/products/IW612)：HTTP Error 404: Not Found。

---

[上一章](P135_NXP_BTB-44_OV5640_Camera_Module.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P137_NXP_M.2_Wi-Fi_and_BT_Shield.md)
