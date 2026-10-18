---
id: learning.zephyr-docs.boards-microchip.page-25
title: PIC64GX1000 Curiosity kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/pic64gx_curiosity_kit/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pic64gx_curiosity_kit"></a>

# 第25章\_PIC64GX1000 Curiosity套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/pic64gx_curiosity_kit/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/pic64gx_curiosity_kit.webp](images/pic64gx_curiosity_kit.webp)](images/pic64gx_curiosity_kit.webp)

PIC64GX1000 Curiosity套件

名称（Name）：

`pic64gx_curiosity_kit`

厂商（Vendor）：

[微芯科技（Microchip Technology Inc.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=microchip)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[pic64gx1000](https://docs.zephyrproject.org/latest/boards/index.html#soc=pic64gx1000)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/pic64gx_curiosity_kit/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Microchip pic64gx_curiosity_kit是基于RISC-V的开发板，搭载Microchip PIC64GX1000 SoC。更多信息见[Microchip网站](https://www.microchip.com/en-us/development-tool/curiosity-pic64gx1000-kit)。

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

<a id="building"></a>

### 构建（Building）

pic64gx_curiosity_kit开发板配置可按通常方式构建应用，参见[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)：

```text
west build -b pic64gx_curiosity_kit/pic64gx1000/u54
```

```text
west build -b pic64gx_curiosity_kit/pic64gx1000/u54/smp
```

<a id="flashing"></a>

### 烧录（Flashing）

向设备加载程序最方便的方法是使用SD卡。SD卡上的二进制文件可由引导加载程序（Bootloader）加载到指定地址。

要让引导加载程序加载应用，需要先生成载荷文件（Payload），步骤如下：

克隆以下仓库并构建工具，以获得hss-payload-generator：

```text
git clone https://github.com/pic64gx/pic64gx-hart-software-services.git
cd pic64gx-hart-software-services/tools/hss-payload-generator
make
```

生成载荷（Payload）：

```text
./hss-payload-generator -c config.yaml -v output.bin
```

使用如下载荷生成器配置文件，生成兼容Hart Software Services（HSS）的载荷：[https://github.com/pic64gx/pic64gx-hart-software-services](https://github.com/pic64gx/pic64gx-hart-software-services)

单核运行（Single Core）：

```text
set-name: 'Zephyr-DDR'

hart-entry-points: {
   u54_1: '0x80000000'
}

payloads:
   build/zephyr/zephyr.elf:    {
      exec-addr: '0x80000000',
      owner-hart: u54_1,
      priv-mode: prv_m,
      skip-opensbi: true,
      payload-name: "zephyr"
   }
```

对称多处理（SMP）：

```text
set-name: 'Zephyr-SMP-DDR'

hart-entry-points: {
   u54_1: '0x80000000',
   u54_2: '0x80000000',
   u54_3: '0x80000000',
   u54_4: '0x80000000'
}

payloads:
   build/zephyr/zephyr.elf:    {
      exec-addr: '0x80000000',
      owner-hart: u54_1,
      secondary-hart: u54_2,
      secondary-hart: u54_3,
      secondary-hart: u54_4,
      priv-mode: prv_m,
      skip-opensbi: true,
      payload-name: "zephyr"
   }
```

载荷生成详情见以下README.md：[https://github.com/pic64gx/pic64gx-hart-software-services/blob/pic64gx/tools/hss-payload-generator/README.md](https://github.com/pic64gx/pic64gx-hart-software-services/blob/pic64gx/tools/hss-payload-generator/README.md)

随后将输出的载荷文件复制到SD卡。原文假设SD卡设备为/dev/sdx；执行示例前应确认实际目标设备。

```text
sudo dd if=<output_payload_file> of=/dev/sdx
```

<a id="debugging"></a>

### 调试（Debugging）

注意，多数情况下应用必须加载到外部DDR存储器，因此加载或调试应用前必须初始化DDR。

先加载HSS固件，再按“[烧录（Flashing）](#flashing)”中的步骤，通过HSS加载器将应用加载到DDR。

随后按通常方式调试应用，参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

## 译注

多数场景需先由HSS初始化外部DDR，再加载或调试Zephyr。/dev/sdx是官方示例中的SD卡设备占位符，写入前必须核对实际设备；本次仅翻译，没有执行写盘命令。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [curiosity-pic64gx1000-kit](https://www.microchip.com/en-us/development-tool/curiosity-pic64gx1000-kit)：HTTP Error 403: Forbidden。

---

[上一章](P024_PIC32CZ_CA90_Curiosity_Ultra.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P026_SAM_E54_Curiosity_Ultra.md)
