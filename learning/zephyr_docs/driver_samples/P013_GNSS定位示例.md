---
id: learning.zephyr-docs.driver_samples.page-13
title: GNSS定位示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/gnss/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="gnss"></a>

# 第13章\_GNSS定位示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/gnss/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 13.1\_概览（Overview）

本例演示使用实现全球卫星导航系统（Global Navigation Satellite System，GNSS）驱动API的设备。

<a id="requirements"></a>

## 13.2\_要求（Requirements）

开发板上必须存在GNSS设备，并在设备树（Devicetree）中启用。

> 译注——实现定位：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gnss/src/main.c)通过gnss设备树别名选取设备，并注册定位数据与卫星信息回调。仅有硬件接线还不足以建立该别名和驱动配置；所用板应具备相应设备树描述。本页原文没有给出普通GNSS构建命令，不虚构通用板目标。

<a id="sample-output"></a>

## 13.3\_示例输出（Sample Output）

```text
gnss: gnss_info: {satellites_cnt: 14, hdop: 0.850, fix_status: GNSS_FIX, fix_quality: GNSS_SPS}
gnss: navigation_data: {latitude: 57.162331699, longitude : 9.961104199, bearing 12.530, speed 0.25, altitude: 42.372}
gnss: gnss_time: {hour: 16, minute: 17, millisecond 36000, month_day 3, month: 10, century_year: 23}
gnss has fix!
gnss: gnss_satellite: {prn: 1, snr: 30, elevation 71, azimuth 276, system: GLONASS, is_tracked: 1}
gnss: gnss_satellite: {prn: 11, snr: 31, elevation 62, azimuth 221, system: GLONASS, is_tracked: 1}
gnss reported 2 satellites (of which 2 tracked, of which 0 has RTK corrections)!
```

> 译注——字段阅读：satellites_cnt为卫星数量，hdop为水平精度因子（Horizontal Dilution of Precision，HDOP），fix_status／fix_quality为定位状态／质量。navigation_data含纬度latitude、经度longitude、航向bearing、速度speed及高度altitude；gnss_time记录时间和日期。单星条目的prn为卫星标识，snr为信噪比（Signal-to-Noise Ratio，SNR），elevation／azimuth为仰角／方位角，system为卫星系统，is_tracked表示是否跟踪。日志先出现14颗卫星的定位信息，后一次卫星报告只有2颗；这是原文各条消息的内容，不能擅自改成同一个数量。末行说明这2颗均被跟踪，且没有RTK改正信息。

<a id="real-time-kinematics-rtk"></a>

## 13.4\_实时动态定位（Real-Time Kinematics (RTK)）

本例也可配置实时动态定位（Real-Time Kinematics，RTK），借助本地基站（Base Station）提高定位精度。

<a id="rtk-requirements"></a>

## 13.5\_RTK要求（RTK Requirements）

需要如下组合：

- 一个连接到开发板的UBlox F9P GNSS模块，作为移动站（Rover）。
- 第二个连接到计算机的UBlox F9P模块，作为基站。

<a id="base-station-setup"></a>

## 13.6\_基站设置（Base Station Setup）

启用RTK时：

1. 通过USB把基站F9P连接到计算机。
2. 同时通过USB把运行本例的移动站串口连接到计算机。
3. 记录移动站连接的串口，例如 `/dev/ttyUSB0`。
4. 运行基站脚本：

```bash
python3 base_station/base_station_f9p.py --port /dev/ttyUSB0
```

脚本把F9P配置为基站，将RTCM3改正数据（Correction Data）流发送到移动站。基站会先执行测量定位（Survey-in）过程，确定自身精确位置，再开始发送改正信息。

> 译注——工作目录与端口角色：这条主机Python命令从samples/drivers/gnss目录执行，base_station/base_station_f9p.py是该示例随附文件。所读[脚本](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gnss/base_station/base_station_f9p.py)把--port用于移动站端口，而基站端口按USB VID 0x1546、PID 0x01A9自动查找；两端都以115200波特打开。因此不要把--port误填成基站端口。/dev/ttyUSB0是原Linux设备示例，应使用主机实际枚举的移动站设备。

> 译注——Python前提：随附[requirements.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gnss/base_station/requirements.txt)列出pyubx2、pyrtcm和pyserial依赖。先在所选主机Python环境准备这些依赖并核对两个端口，再启动脚本；端口未找到时先解决设备枚举和权限。本批未安装依赖、连接接收机、启动survey-in或传输改正数据。

<a id="see-also"></a>

## 13.7\_相关接口（See also）

[GNSS接口](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html)、[导航（Navigation）接口](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html)。


对应官方文档源码：[samples/drivers/gnss/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/gnss/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/gnss/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/gnss/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P012_I2S示例目录.md) · [返回大纲](大纲.md) · [下一章](P014_LoRa示例目录.md)
