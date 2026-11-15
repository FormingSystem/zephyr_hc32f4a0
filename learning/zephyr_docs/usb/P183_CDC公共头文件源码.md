---
id: learning.zephyr-docs.usb.api-183
title: CDC公共头文件源码
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__cdc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_CDC公共头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__cdc_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 183.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

下方保留官方 Doxygen 源码浏览页的全部代码和许可注释。仅移除网页行号、还原显示用空格并清理行尾空白；原页省略的 API 注释由[CDC 公共头文件与常量](P174_CDC公共头文件与常量.md)及本组结构参考承接。源码展示不冒充带有全部注释的原始头文件。

## 183.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="foldopen00285"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00311"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="foldopen00319"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="foldopen00329"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcdc__acm__descriptor_html"></a>
<a id="astructcdc__acm__descriptor_html_a3066a08cbc5f0747d435a13ee4f22d14"></a>
<a id="astructcdc__acm__descriptor_html_a665260ce8cc55e35c941078987f92366"></a>
<a id="astructcdc__acm__descriptor_html_ab62800772430a82673004fcaac13c071"></a>
<a id="astructcdc__acm__descriptor_html_ae1011a0e1520193be5c1fb0fe442915e"></a>
<a id="astructcdc__acm__line__coding_html"></a>
<a id="astructcdc__acm__line__coding_html_a14d35b67e6f00b0d6196ba0e9ef6dfab"></a>
<a id="astructcdc__acm__line__coding_html_a472270d84e160348e024f756b834cbb8"></a>
<a id="astructcdc__acm__line__coding_html_ab685d018d83e3e2d38c87c27902cca3e"></a>
<a id="astructcdc__acm__line__coding_html_afd2fd70a7da783d7aac0d99f9f267383"></a>
<a id="astructcdc__acm__notification_html"></a>
<a id="astructcdc__acm__notification_html_a290717590343376c8f1f9a865cb4b0ae"></a>
<a id="astructcdc__acm__notification_html_a3bf290bc6e851331e93bedf49ae5dbe0"></a>
<a id="astructcdc__acm__notification_html_a5666402ce9fbe5fad5f80592aa6f53ec"></a>
<a id="astructcdc__acm__notification_html_a57b007a8ec893d660e6ec8a1b25f7dd3"></a>
<a id="astructcdc__acm__notification_html_af24dae76a280c008e40a0d031171235c"></a>
<a id="astructcdc__acm__notification_html_af2f8fbceeaa9a3ad0ae1330b8f82bff2"></a>
<a id="astructcdc__cm__descriptor_html"></a>
<a id="astructcdc__cm__descriptor_html_a0a29f8dfe1dd9758f210b63d7a87bdc6"></a>
<a id="astructcdc__cm__descriptor_html_a578a2a39c7c80de58cb7d952f8decd22"></a>
<a id="astructcdc__cm__descriptor_html_a908003360bca9ab79f55d80a2fc7aa24"></a>
<a id="astructcdc__cm__descriptor_html_aabbca6f88b936659124aa28264054b6d"></a>
<a id="astructcdc__cm__descriptor_html_ad40616645c5b28754300594b43805a1f"></a>
<a id="astructcdc__ecm__descriptor_html"></a>
<a id="astructcdc__ecm__descriptor_html_a196fcac7b1c9bf0f2b42a6d4ccb48de6"></a>
<a id="astructcdc__ecm__descriptor_html_a3a7b901bef04212b217a69d055e37e66"></a>
<a id="astructcdc__ecm__descriptor_html_aa5cfb3a02e9818cf3faaff1dbb9dd487"></a>
<a id="astructcdc__ecm__descriptor_html_aaf95074ec751f227a33317325567c890"></a>
<a id="astructcdc__ecm__descriptor_html_ad43f97e428ef743d4655a1e91b91478d"></a>
<a id="astructcdc__ecm__descriptor_html_ae000bdad185ca5af3674274ea3fa45d6"></a>
<a id="astructcdc__ecm__descriptor_html_aed687a9629eb3c793af9260db407a136"></a>
<a id="astructcdc__ecm__descriptor_html_afdf7f4478515917b1ed653118e7a8540"></a>
<a id="astructcdc__header__descriptor_html"></a>
<a id="astructcdc__header__descriptor_html_a3b8cc0d8b9d56db158f3b027b2cd6f6a"></a>
<a id="astructcdc__header__descriptor_html_a49bf7e700891057f30cd3be77dec0752"></a>
<a id="astructcdc__header__descriptor_html_ab66b3b87594a4510f11ba9ee950f230c"></a>
<a id="astructcdc__header__descriptor_html_ac4ad6939d5a075ff2fe6d7505cba630b"></a>
<a id="astructcdc__ncm__descriptor_html"></a>
<a id="astructcdc__ncm__descriptor_html_a8a88e3d7d2b36876a38fa8025118f069"></a>
<a id="astructcdc__ncm__descriptor_html_a932a73d95abf90a0ba7f0de3e1760375"></a>
<a id="astructcdc__ncm__descriptor_html_a9dea58db91413ebcff65151e006a3b2c"></a>
<a id="astructcdc__ncm__descriptor_html_a9fb11a778a65e5e8538619467cd6c6d6"></a>
<a id="astructcdc__ncm__descriptor_html_aa9b5bd71a73783e4a3c85a1d39f9def3"></a>
<a id="astructcdc__union__descriptor_html"></a>
<a id="astructcdc__union__descriptor_html_a5bab5215179ecc0bb0bb6e7b9089abf6"></a>
<a id="astructcdc__union__descriptor_html_a81bdab223598b27b620de0d9dba7bc80"></a>
<a id="astructcdc__union__descriptor_html_a839a6a4a7c4b2618c49649d93b7c6ff9"></a>
<a id="astructcdc__union__descriptor_html_a83ee5a04668006397663142232471606"></a>
<a id="astructcdc__union__descriptor_html_a965212d833550c13376b231d5e2ce125"></a>

```c
/* usb_cdc.h - USB CDC-ACM and CDC-ECM public header */

/*
 * Copyright (c) 2017 PHYTEC Messtechnik GmbH
 * Copyright (c) 2025 - 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_INCLUDE_USB_CLASS_USB_CDC_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USB_CDC_H_

#define CDC_SRN_1_20                    0x0120 __DEPRECATED_MACRO

#define ACM_SUBCLASS                    0x02
#define ECM_SUBCLASS                    0x06
#define EEM_SUBCLASS                    0x0c
#define NCM_SUBCLASS                    0x0d

#define AT_CMD_V250_PROTOCOL            0x01
#define EEM_PROTOCOL                    0x07
#define ACM_VENDOR_PROTOCOL             0xFF
#define NCM_DATA_PROTOCOL               0x01

#define DATA_INTERFACE_CLASS            0x0A

#define HEADER_FUNC_DESC                0x00
#define CALL_MANAGEMENT_FUNC_DESC       0x01
#define ACM_FUNC_DESC                   0x02
#define UNION_FUNC_DESC                 0x06
#define ETHERNET_FUNC_DESC              0x0F
#define ETHERNET_FUNC_DESC_NCM          0x1a


#define USB_CDC_NETWORK_CONNECTION      0x00
#define USB_CDC_RESPONSE_AVAILABLE      0x01
#define USB_CDC_CONNECTION_SPEED_CHANGE 0x2A

#define CDC_SEND_ENC_CMD                0x00
#define CDC_GET_ENC_RSP                 0x01
#define SET_LINE_CODING                 0x20
#define GET_LINE_CODING                 0x21
#define SET_CONTROL_LINE_STATE          0x22


#define USB_CDC_AUX_JACK_HOOK_STATE     0x08
#define USB_CDC_RING_DETECT             0x09
#define USB_CDC_SERIAL_STATE            0x20
#define USB_CDC_LINE_STATE_CHANGE       0x23
#define USB_CDC_CALL_STATE_CHANGE       0x28

#define USB_CDC_SERIAL_STATE_OVERRUN    BIT(6)
#define USB_CDC_SERIAL_STATE_PARITY     BIT(5)
#define USB_CDC_SERIAL_STATE_FRAMING    BIT(4)
#define USB_CDC_SERIAL_STATE_RINGSIGNAL BIT(3)
#define USB_CDC_SERIAL_STATE_BREAK      BIT(2)
#define USB_CDC_SERIAL_STATE_TXCARRIER  BIT(1)
#define USB_CDC_SERIAL_STATE_RXCARRIER  BIT(0)

#define SET_CONTROL_LINE_STATE_RTS      0x02
#define SET_CONTROL_LINE_STATE_DTR      0x01

#define USB_CDC_LINE_CTRL_BAUD_RATE     UART_LINE_CTRL_BAUD_RATE
#define USB_CDC_LINE_CTRL_DCD           UART_LINE_CTRL_DCD
#define USB_CDC_LINE_CTRL_DSR           UART_LINE_CTRL_DSR
#define USB_CDC_LINE_CTRL_BREAK         BIT(5)
#define USB_CDC_LINE_CTRL_RING_SIGNAL   BIT(6)
#define USB_CDC_LINE_CTRL_FRAMING       BIT(7)
#define USB_CDC_LINE_CTRL_PARITY        BIT(8)
#define USB_CDC_LINE_CTRL_OVER_RUN      BIT(9)

#define SERIAL_STATE_OVER_RUN           0x40
#define SERIAL_STATE_PARITY             0x20
#define SERIAL_STATE_FRAMING            0x10
#define SERIAL_STATE_RING_SIGNAL        0x08
#define SERIAL_STATE_BREAK              0x04
#define SERIAL_STATE_TX_CARRIER         0x02
#define SERIAL_STATE_RX_CARRIER         0x01

#define USB_CDC_LINE_CODING_STOP_BITS_1         0
#define USB_CDC_LINE_CODING_STOP_BITS_1_5       1
#define USB_CDC_LINE_CODING_STOP_BITS_2         2

#define USB_CDC_LINE_CODING_PARITY_NO           0
#define USB_CDC_LINE_CODING_PARITY_ODD          1
#define USB_CDC_LINE_CODING_PARITY_EVEN         2
#define USB_CDC_LINE_CODING_PARITY_MARK         3
#define USB_CDC_LINE_CODING_PARITY_SPACE        4

#define USB_CDC_LINE_CODING_DATA_BITS_5         5
#define USB_CDC_LINE_CODING_DATA_BITS_6         6
#define USB_CDC_LINE_CODING_DATA_BITS_7         7
#define USB_CDC_LINE_CODING_DATA_BITS_8         8

#define SET_ETHERNET_MULTICAST_FILTERS  0x40
#define SET_ETHERNET_PM_FILTER          0x41
#define GET_ETHERNET_PM_FILTER          0x42
#define SET_ETHERNET_PACKET_FILTER      0x43
#define GET_ETHERNET_STATISTIC          0x44

#define GET_NTB_PARAMETERS     0x80
#define GET_NET_ADDRESS        0x81
#define SET_NET_ADDRESS        0x82
#define GET_NTB_FORMAT         0x83
#define SET_NTB_FORMAT         0x84
#define GET_NTB_INPUT_SIZE     0x85
#define SET_NTB_INPUT_SIZE     0x86
#define GET_MAX_DATAGRAM_SIZE  0x87
#define SET_MAX_DATAGRAM_SIZE  0x88
#define GET_CRC_MODE           0x89
#define SET_CRC_MODE           0x8A

#define USB_CDC_NCM_NCAP_ETH_FILTER             BIT(0)
#define USB_CDC_NCM_NCAP_NET_ADDRESS            BIT(1)
#define USB_CDC_NCM_NCAP_ENCAP_COMMAND          BIT(2)
#define USB_CDC_NCM_NCAP_MAX_DATAGRAM_SIZE      BIT(3)
#define USB_CDC_NCM_NCAP_CRC_MODE               BIT(4)
#define USB_CDC_NCM_NCAP_NTB_INPUT_SIZE         BIT(5)

#define PACKET_TYPE_MULTICAST           0x10
#define PACKET_TYPE_BROADCAST           0x08
#define PACKET_TYPE_DIRECTED            0x04
#define PACKET_TYPE_ALL_MULTICAST       0x02
#define PACKET_TYPE_PROMISCUOUS         0x01


#define USB_CDC_ECM_STAT_RESERVED               0x00
#define USB_CDC_ECM_STAT_XMIT_OK                0x01
#define USB_CDC_ECM_STAT_RCV_OK                 0x02
#define USB_CDC_ECM_STAT_XMIT_ERROR             0x03
#define USB_CDC_ECM_STAT_RCV_ERROR              0x04
#define USB_CDC_ECM_STAT_RCV_NO_BUFFER          0x05
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_XMIT    0x06
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_XMIT   0x07
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_XMIT   0x08
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_XMIT  0x09
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_XMIT   0x0A
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_XMIT  0x0B
#define USB_CDC_ECM_STAT_DIRECTED_BYTES_RCV     0x0C
#define USB_CDC_ECM_STAT_DIRECTED_FRAMES_RCV    0x0D
#define USB_CDC_ECM_STAT_MULTICAST_BYTES_RCV    0x0E
#define USB_CDC_ECM_STAT_MULTICAST_FRAMES_RCV   0x0F
#define USB_CDC_ECM_STAT_BROADCAST_BYTES_RCV    0x10
#define USB_CDC_ECM_STAT_BROADCAST_FRAMES_RCV   0x11
#define USB_CDC_ECM_STAT_RCV_CRC_ERROR          0x12
#define USB_CDC_ECM_STAT_TRANSMIT_QUEUE_LENGTH  0x13
#define USB_CDC_ECM_STAT_RCV_ERROR_ALIGNMENT    0x14
#define USB_CDC_ECM_STAT_XMIT_ONE_COLLISION     0x15
#define USB_CDC_ECM_STAT_XMIT_MORE_COLLISIONS   0x16
#define USB_CDC_ECM_STAT_XMIT_DEFERRED          0x17
#define USB_CDC_ECM_STAT_XMIT_MAX_COLLISIONS    0x18
#define USB_CDC_ECM_STAT_RCV_OVERRUN            0x19
#define USB_CDC_ECM_STAT_XMIT_UNDERRUN          0x1A
#define USB_CDC_ECM_STAT_XMIT_HEARTBEAT_FAILURE 0x1B
#define USB_CDC_ECM_STAT_XMIT_TIMES_CRS_LOST    0x1C
#define USB_CDC_ECM_STAT_XMIT_LATE_COLLISIONS   0x1D

struct cdc_header_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint16_t bcdCDC;
} __packed;

struct cdc_union_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint8_t bControlInterface;
        uint8_t bSubordinateInterface0;
} __packed;

struct cdc_cm_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint8_t bmCapabilities;
        uint8_t bDataInterface;
} __packed;

struct cdc_acm_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint8_t bmCapabilities;
} __packed;

struct cdc_acm_line_coding {
        uint32_t dwDTERate;
        uint8_t bCharFormat;
        uint8_t bParityType;
        uint8_t bDataBits;
} __packed;

struct cdc_acm_notification {
        uint8_t bmRequestType;
        uint8_t bNotificationType;
        uint16_t wValue;
        uint16_t wIndex;
        uint16_t wLength;
        uint16_t data;
} __packed;

struct cdc_ecm_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint8_t iMACAddress;
        uint32_t bmEthernetStatistics;
        uint16_t wMaxSegmentSize;
        uint16_t wNumberMCFilters;
        uint8_t bNumberPowerFilters;
} __packed;

struct cdc_ncm_descriptor {
        uint8_t bFunctionLength;
        uint8_t bDescriptorType;
        uint8_t bDescriptorSubtype;
        uint16_t bcdNcmVersion;
        uint8_t bmNetworkCapabilities;
} __packed;

#endif /* ZEPHYR_INCLUDE_USB_CLASS_USB_CDC_H_ */
```

## 183.3\_源码注释与阅读说明

开头的 usb_cdc.h 注释意为“USB CDC-ACM 和 CDC-ECM 公共头文件”。原始署名为 Copyright (c) 2017 PHYTEC Messtechnik GmbH 及 Copyright (c) 2025 - 2026 NXP，许可证标识为 `Apache-2.0`，均在代码中逐字保留。

`ZEPHYR_INCLUDE_USB_CLASS_USB_CDC_H_` 是头文件包含保护（Header Include Guard）；结尾同名注释标明所关闭的条件分支。各结构的 `__packed` 标记保持原样，描述符字段、线路编码和通知载荷应按各自协议解释，不能仅按相似名称互换。

## 183.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

[上一章](P182_CDC网络控制模型描述符.md) · [返回大纲](大纲.md) · [下一章](P184_DFU公共常量与状态码.md)
