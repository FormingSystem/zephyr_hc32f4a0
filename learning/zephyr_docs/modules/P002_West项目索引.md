---
id: learning.zephyr-docs.modules.page-2
title: West项目索引
kind: reference
status: maintained
domains: [zephyr, modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="west-projects-index"></a>
<a id="id1"></a>

# 第2章\_West项目索引

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/index.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 2.1\_索引用途

本页汇集与[west元工具（Meta-tool）](../west/P014_west官方总入口.md#west)兼容的项目／模块（Project／Module）。主要列出Zephyr默认[清单文件（Manifest File）](https://github.com/zephyrproject-rtos/zephyr/blob/main/west.yml)声明的组件。关于这些导入组件的贡献与审查流程，参见[贡献外部组件](../contributing/P012_外部组件贡献.md#external-contributions)。

本页还维护由Zephyr项目之外的团队维护、可方便地接入Zephyr工作区的[外部项目](#west-external-projects)目录。

> 译注——快照与本地状态：以下名称、分类及40位提交号完整保留自本次读取的官网页面。它们描述该页面所用清单，不代表读者当前活动清单或实际检出的版本，也不表示这些组件的全部文档已经翻译。对照时先确认自己的活动清单；原文件只读查看，不用下面的列表替换已有west.yml。

<a id="active-projects-modules"></a>

## 2.2\_活动项目与模块（Active Projects/Modules）

以下项目默认启用，在执行 `west update` 时下载。许多项目／模块是构建通用Zephyr应用所必需的，其中包括Zephyr多种平台的硬件支持。

若要禁用一个活动模块，例如特定硬件抽象层（Hardware Abstraction Layer，HAL），原文使用：

```bash
west config manifest.project-filter -- -hal_FOO
west update
```

> 译注——运行位置与配置：这是已有west工作区中的命令，hal_FOO须替换为实际项目名称。west config修改的是工作区配置，west update随后依据有效清单和筛选结果更新依赖；禁用项目不会等同于删除磁盘上已有目录。manifest.project-filter是按名称匹配的正则表达式列表，规则按顺序处理，最后一个匹配生效。已有过滤设置应先查看并合并，不能无意覆盖其他选择，详见[west配置](../west/P003_配置.md)。本批没有运行这些命令。

| 项目（Project） | 修订版本（Revision） |
| --- | --- |
| `acpica` | [8d24867bc9c9d81c81eeac59391cda59333affd4](https://github.com/zephyrproject-rtos/acpica/commit/8d24867bc9c9d81c81eeac59391cda59333affd4) |
| `cmsis` | [512cc7e895e8491696b61f7ba8066b4a182569b8](https://github.com/zephyrproject-rtos/cmsis/commit/512cc7e895e8491696b61f7ba8066b4a182569b8) |
| `cmsis-dsp` | [45d23287f5b41be49612281a5e7c802c6a415388](https://github.com/zephyrproject-rtos/cmsis-dsp/commit/45d23287f5b41be49612281a5e7c802c6a415388) |
| `cmsis-nn` | [73591f72850bfebe95c6f30f6e75a773abb711cd](https://github.com/zephyrproject-rtos/cmsis-nn/commit/73591f72850bfebe95c6f30f6e75a773abb711cd) |
| `cmsis_6` | [1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8](https://github.com/zephyrproject-rtos/CMSIS_6/commit/1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8) |
| `dhara` | [6f163ca05e174b168b4d148160b50eeaeeb561fc](https://github.com/zephyrproject-rtos/dhara/commit/6f163ca05e174b168b4d148160b50eeaeeb561fc) |
| `edtt` | [c282625e694f0b53ea53e13231ea6d2f49411768](https://github.com/zephyrproject-rtos/edtt/commit/c282625e694f0b53ea53e13231ea6d2f49411768) |
| `fatfs` | [4f60a12c58c3de4246857ad87c40239ecd93349b](https://github.com/zephyrproject-rtos/fatfs/commit/4f60a12c58c3de4246857ad87c40239ecd93349b) |
| `hal_adi` | [489885cdfa668870f95b00ded1cc56ac52cdf5c4](https://github.com/zephyrproject-rtos/hal_adi/commit/489885cdfa668870f95b00ded1cc56ac52cdf5c4) |
| `hal_afbr` | [effa58cab4a5e5f38d03357c73a65600d7414a67](https://github.com/zephyrproject-rtos/hal_afbr/commit/effa58cab4a5e5f38d03357c73a65600d7414a67) |
| `hal_ambiq` | [3d7044ea240fc8dcb7b4c843b76f70cae5db736b](https://github.com/zephyrproject-rtos/hal_ambiq/commit/3d7044ea240fc8dcb7b4c843b76f70cae5db736b) |
| `hal_atmel` | [8f95c79f2a80427ef446563cc9addefa959e92a9](https://github.com/zephyrproject-rtos/hal_atmel/commit/8f95c79f2a80427ef446563cc9addefa959e92a9) |
| `hal_bouffalolab` | [577b219696191f7715ac772e265b14108ecc49a5](https://github.com/zephyrproject-rtos/hal_bouffalolab/commit/577b219696191f7715ac772e265b14108ecc49a5) |
| `hal_espressif` | [b16851b3c20e6fad3d2da42ec24a3e82d0b8b444](https://github.com/zephyrproject-rtos/hal_espressif/commit/b16851b3c20e6fad3d2da42ec24a3e82d0b8b444) |
| `hal_ethos_u` | [5f0b9d1e17b245aefc308ee0d5a4543833b96b11](https://github.com/zephyrproject-rtos/hal_ethos_u/commit/5f0b9d1e17b245aefc308ee0d5a4543833b96b11) |
| `hal_gigadevice` | [804f92bf5794e403fab89178dcc6d775b9269c0d](https://github.com/zephyrproject-rtos/hal_gigadevice/commit/804f92bf5794e403fab89178dcc6d775b9269c0d) |
| `hal_infineon` | [2191db4d7723737ffd3d59d01b50f7595dac2944](https://github.com/zephyrproject-rtos/hal_infineon/commit/2191db4d7723737ffd3d59d01b50f7595dac2944) |
| `hal_intel` | [884c7a79a48efef50bc0d12c86f5d0951748f24d](https://github.com/zephyrproject-rtos/hal_intel/commit/884c7a79a48efef50bc0d12c86f5d0951748f24d) |
| `hal_microchip` | [e33b6fce18d8a75dad23a2af6dd2d027564fee89](https://github.com/zephyrproject-rtos/hal_microchip/commit/e33b6fce18d8a75dad23a2af6dd2d027564fee89) |
| `hal_nordic` | [c708b9fe1b7a36090c468374811a6e934b97e54a](https://github.com/zephyrproject-rtos/hal_nordic/commit/c708b9fe1b7a36090c468374811a6e934b97e54a) |
| `hal_nuvoton` | [0f411a85da7d17a612d54450f608f4d30cdb971f](https://github.com/zephyrproject-rtos/hal_nuvoton/commit/0f411a85da7d17a612d54450f608f4d30cdb971f) |
| `hal_nxp` | [a8b437ef366ff9a6f9bee3377dc189c4d2623f5b](https://github.com/zephyrproject-rtos/hal_nxp/commit/a8b437ef366ff9a6f9bee3377dc189c4d2623f5b) |
| `hal_openisa` | [eabd530a64d71de91d907bad257cd61aacf607bc](https://github.com/zephyrproject-rtos/hal_openisa/commit/eabd530a64d71de91d907bad257cd61aacf607bc) |
| `hal_quicklogic` | [bad894440fe72c814864798c8e3a76d13edffb6c](https://github.com/zephyrproject-rtos/hal_quicklogic/commit/bad894440fe72c814864798c8e3a76d13edffb6c) |
| `hal_realtek` | [29d365ccfbceb9f42ce666d75463fbe2c83b8e29](https://github.com/zephyrproject-rtos/hal_realtek/commit/29d365ccfbceb9f42ce666d75463fbe2c83b8e29) |
| `hal_renesas` | [4f84c164c0f298dd2ffd806521ef66320a0bf3b1](https://github.com/zephyrproject-rtos/hal_renesas/commit/4f84c164c0f298dd2ffd806521ef66320a0bf3b1) |
| `hal_rpi_pico` | [2e9dbf14fa56e5907aefb07e8e75010ec5210946](https://github.com/zephyrproject-rtos/hal_rpi_pico/commit/2e9dbf14fa56e5907aefb07e8e75010ec5210946) |
| `hal_sifli` | [86fa0e9433fda1a760e0077c19b8407ecceea2f9](https://github.com/zephyrproject-rtos/hal_sifli/commit/86fa0e9433fda1a760e0077c19b8407ecceea2f9) |
| `hal_silabs` | [ca5f98ea5588fd6aefcb03cb6ea9898ed90ecf15](https://github.com/zephyrproject-rtos/hal_silabs/commit/ca5f98ea5588fd6aefcb03cb6ea9898ed90ecf15) |
| `hal_st` | [ce795a9b0de623022c17d2ff394587c024aec850](https://github.com/zephyrproject-rtos/hal_st/commit/ce795a9b0de623022c17d2ff394587c024aec850) |
| `hal_stm32` | [c9550199186236d610092f4005f8c9bae2a6bfcf](https://github.com/zephyrproject-rtos/hal_stm32/commit/c9550199186236d610092f4005f8c9bae2a6bfcf) |
| `hal_tdk` | [4e53fe1a1ea634dd8a13ecda1151a73bc598622f](https://github.com/zephyrproject-rtos/hal_tdk/commit/4e53fe1a1ea634dd8a13ecda1151a73bc598622f) |
| `hal_telink` | [4226c7fc17d5a34e557d026d428fc766191a0800](https://github.com/zephyrproject-rtos/hal_telink/commit/4226c7fc17d5a34e557d026d428fc766191a0800) |
| `hal_ti` | [53c80140dd69905cc5e034f637eff9c66b2f9654](https://github.com/zephyrproject-rtos/hal_ti/commit/53c80140dd69905cc5e034f637eff9c66b2f9654) |
| `hal_wch` | [fbfabfc590e86b74af873bd26d3b4433a0ffb9e9](https://github.com/zephyrproject-rtos/hal_wch/commit/fbfabfc590e86b74af873bd26d3b4433a0ffb9e9) |
| `hal_wurthelektronik` | [7c1297ea071d03289112eb24e789c89c7095c0a2](https://github.com/zephyrproject-rtos/hal_wurthelektronik/commit/7c1297ea071d03289112eb24e789c89c7095c0a2) |
| `hal_xtensa` | [60224c27bed1466287f0246ac04c902b92331c29](https://github.com/zephyrproject-rtos/hal_xtensa/commit/60224c27bed1466287f0246ac04c902b92331c29) |
| `hostap` | [33921a8a77c56bddfe196a11935009cededc3bb3](https://github.com/zephyrproject-rtos/hostap/commit/33921a8a77c56bddfe196a11935009cededc3bb3) |
| `liblc3` | [48bbd3eacd36e99a57317a0a4867002e0b09e183](https://github.com/zephyrproject-rtos/liblc3/commit/48bbd3eacd36e99a57317a0a4867002e0b09e183) |
| `libmctp` | [b6be45dfc5c67c43c3a5e12589ae3845ea00ab5e](https://github.com/zephyrproject-rtos/libmctp/commit/b6be45dfc5c67c43c3a5e12589ae3845ea00ab5e) |
| `libmetal` | [77237e9748212796a8f93a33689ce935fb9c81c2](https://github.com/zephyrproject-rtos/libmetal/commit/77237e9748212796a8f93a33689ce935fb9c81c2) |
| `libsbc` | [8e1beda02acb8972e29e6edbb423f7cafe16e445](https://github.com/zephyrproject-rtos/libsbc/commit/8e1beda02acb8972e29e6edbb423f7cafe16e445) |
| `littlefs` | [e9a8638fc228e43a3156ed3ac602229af3e3c1d5](https://github.com/zephyrproject-rtos/littlefs/commit/e9a8638fc228e43a3156ed3ac602229af3e3c1d5) |
| `lora-basics-modem` | [a8ddc544043e72807cf7db532478e1dda734ae7c](https://github.com/zephyrproject-rtos/lora-basics-modem/commit/a8ddc544043e72807cf7db532478e1dda734ae7c) |
| `loramac-node` | [874544f2a8a0212a0cc12e5eea51a024fd3d93d1](https://github.com/zephyrproject-rtos/loramac-node/commit/874544f2a8a0212a0cc12e5eea51a024fd3d93d1) |
| `lvgl` | [c9ffd4692de246eb911c7ba49b78a331b2c63c74](https://github.com/zephyrproject-rtos/lvgl/commit/c9ffd4692de246eb911c7ba49b78a331b2c63c74) |
| `mbedtls` | [c43f34b93797e81fd0257c30004dcd0ae332ae51](https://github.com/zephyrproject-rtos/mbedtls/commit/c43f34b93797e81fd0257c30004dcd0ae332ae51) |
| `mcuboot` | [bfbc2eff1ab2f8d290b915036ecdaafdbc620e0f](https://github.com/zephyrproject-rtos/mcuboot/commit/bfbc2eff1ab2f8d290b915036ecdaafdbc620e0f) |
| `mipi-sys-t` | [5a9d6055b62edc54566d6d0034d9daec91749b98](https://github.com/zephyrproject-rtos/mipi-sys-t/commit/5a9d6055b62edc54566d6d0034d9daec91749b98) |
| `mldsa-native` | [3fc19982839305d305071f0de0c540bc9c9bea8a](https://github.com/zephyrproject-rtos/mldsa-native/commit/3fc19982839305d305071f0de0c540bc9c9bea8a) |
| `nanopb` | [0f6d088e777a33dd7b54297f137ef10d745c5da8](https://github.com/zephyrproject-rtos/nanopb/commit/0f6d088e777a33dd7b54297f137ef10d745c5da8) |
| `net-tools` | [96ecb88c982812d48564d319cf7d9a0709c85c70](https://github.com/zephyrproject-rtos/net-tools/commit/96ecb88c982812d48564d319cf7d9a0709c85c70) |
| `nrf_hw_models` | [50187f3879ffaafc171d364490bead27557f5192](https://github.com/zephyrproject-rtos/nrf_hw_models/commit/50187f3879ffaafc171d364490bead27557f5192) |
| `nrf_wifi` | [fc0872109ec4c006d32843a202b129db33cf16b9](https://github.com/zephyrproject-rtos/nrf_wifi/commit/fc0872109ec4c006d32843a202b129db33cf16b9) |
| `open-amp` | [01032a8a7bdfdd541686f5dfa3671e602b9fcbff](https://github.com/zephyrproject-rtos/open-amp/commit/01032a8a7bdfdd541686f5dfa3671e602b9fcbff) |
| `openthread` | [4a8d33459567cc611bf9d4d810c2201a24a64d84](https://github.com/zephyrproject-rtos/openthread/commit/4a8d33459567cc611bf9d4d810c2201a24a64d84) |
| `percepio` | [022c06f76d3e141aad98252fa9211665bf8ca027](https://github.com/zephyrproject-rtos/percepio/commit/022c06f76d3e141aad98252fa9211665bf8ca027) |
| `picolibc` | [01254932e8e81085817ed61fd858648584ffe37c](https://github.com/zephyrproject-rtos/picolibc/commit/01254932e8e81085817ed61fd858648584ffe37c) |
| `psa-arch-tests` | [3ce2420dd321c86928b40d33a8f799f5138469d3](https://github.com/zephyrproject-rtos/psa-arch-tests/commit/3ce2420dd321c86928b40d33a8f799f5138469d3) |
| `reqmgmt` | [c6803e9b4e9bf9ae7fad3c7cd85dbf35d0d09ede](https://github.com/zephyrproject-rtos/reqmgmt/commit/c6803e9b4e9bf9ae7fad3c7cd85dbf35d0d09ede) |
| `segger` | [50892fdbcf2f570e67baa72b8894a66b16946f72](https://github.com/zephyrproject-rtos/segger/commit/50892fdbcf2f570e67baa72b8894a66b16946f72) |
| `tf-m-tests` | [420c95daa7a25143bb88f807a1e2c432dd4372e8](https://github.com/zephyrproject-rtos/tf-m-tests/commit/420c95daa7a25143bb88f807a1e2c432dd4372e8) |
| `tf-psa-crypto` | [765af96a20a2b408474dcd950372ba9af4d26b62](https://github.com/zephyrproject-rtos/tf-psa-crypto/commit/765af96a20a2b408474dcd950372ba9af4d26b62) |
| `tf-psa-crypto-drivers` | [edb74a92e602cd21a218836aff41a0600229978c](https://github.com/zephyrproject-rtos/tf-psa-crypto-drivers/commit/edb74a92e602cd21a218836aff41a0600229978c) |
| `trusted-firmware-a` | [4d431cbbb451d13359534c63bf67e2d315ca37de](https://github.com/zephyrproject-rtos/trusted-firmware-a/commit/4d431cbbb451d13359534c63bf67e2d315ca37de) |
| `trusted-firmware-m` | [3d46d29fb296af1ff278ea3216e6fe0289a8fa7a](https://github.com/zephyrproject-rtos/trusted-firmware-m/commit/3d46d29fb296af1ff278ea3216e6fe0289a8fa7a) |
| `uoscore-uedhoc` | [dc0ab6345450668de3f9597320a48c5a2d409bb6](https://github.com/zephyrproject-rtos/uoscore-uedhoc/commit/dc0ab6345450668de3f9597320a48c5a2d409bb6) |
| `zcbor` | [9164bd18dcd88ff9d9ef98279501fc1093571017](https://github.com/zephyrproject-rtos/zcbor/commit/9164bd18dcd88ff9d9ef98279501fc1093571017) |
| `zephyr-xenlib` | [8b13d0b709314b7de6cb5877c286d52e71095cc8](https://github.com/zephyrproject-rtos/zephyr-xenlib/commit/8b13d0b709314b7de6cb5877c286d52e71095cc8) |


<a id="inactive-and-optional-projects-modules"></a>

## 2.3\_非活动与可选项目模块（Inactive and Optional Projects/Modules）

以下项目是可选项，默认不会随 `west update` 下载。可以按需加入项目／模块，用于编写应用代码，扩展工作区的功能。

原文给出的启用示例为：

```bash
west config manifest.project-filter -- +nanopb
west update
```

> 译注——示例名称与当前列表：原页本次快照已把nanopb列在上面的活动项目中，但此处仍用它演示加号启用语法。两者原样保留，不能据此判断nanopb在自己的工作区被禁用。应根据实际清单和过滤设置选择需要启用的项目；修改筛选并下载成功也不等于完成应用Kconfig配置或编译验证。

| 项目（Project） | 修订版本（Revision） |
| --- | --- |
| `tflite-micro` | [43b2a106a391dd8a099ac47f2ae858630a397264](https://github.com/zephyrproject-rtos/tflite-micro/commit/43b2a106a391dd8a099ac47f2ae858630a397264) |
| `zephyr-lang-rust` | [dd73abc242e995784da62352fe8c70d9a6c7ac2e](https://github.com/zephyrproject-rtos/zephyr-lang-rust/commit/dd73abc242e995784da62352fe8c70d9a6c7ac2e) |
| `babblesim_base` | [68baf150660213d67c29acb14bf9fccecf4612eb](https://github.com/BabbleSim/base/commit/68baf150660213d67c29acb14bf9fccecf4612eb) |
| `babblesim_ext_2G4_channel_NtNcable` | [20a38c997f507b0aa53817aab3d73a462fff7af1](https://github.com/BabbleSim/ext_2G4_channel_NtNcable/commit/20a38c997f507b0aa53817aab3d73a462fff7af1) |
| `babblesim_ext_2G4_channel_multiatt` | [bde72a57384dde7a4310bcf3843469401be93074](https://github.com/BabbleSim/ext_2G4_channel_multiatt/commit/bde72a57384dde7a4310bcf3843469401be93074) |
| `babblesim_ext_2G4_device_WLAN_actmod` | [9cb6d8e72695f6b785e57443f0629a18069d6ce4](https://github.com/BabbleSim/ext_2G4_device_WLAN_actmod/commit/9cb6d8e72695f6b785e57443f0629a18069d6ce4) |
| `babblesim_ext_2G4_device_burst_interferer` | [5b5339351d6e6a2368c686c734dc8b2fc65698fc](https://github.com/BabbleSim/ext_2G4_device_burst_interferer/commit/5b5339351d6e6a2368c686c734dc8b2fc65698fc) |
| `babblesim_ext_2G4_device_playback` | [abb48cd71ddd4e2a9022f4bf49b2712524c483e8](https://github.com/BabbleSim/ext_2G4_device_playback/commit/abb48cd71ddd4e2a9022f4bf49b2712524c483e8) |
| `babblesim_ext_2G4_libPhyComv1` | [27eb408f952182a646eac1abb7dc12b7b565655b](https://github.com/BabbleSim/ext_2G4_libPhyComv1/commit/27eb408f952182a646eac1abb7dc12b7b565655b) |
| `babblesim_ext_2G4_modem_BLE_simple` | [6fdae81d5b5e348bd130c038d049b233ce983a74](https://github.com/BabbleSim/ext_2G4_modem_BLE_simple/commit/6fdae81d5b5e348bd130c038d049b233ce983a74) |
| `babblesim_ext_2G4_modem_magic` | [d8281acb634895c8a769489c27146bdfe1a54938](https://github.com/BabbleSim/ext_2G4_modem_magic/commit/d8281acb634895c8a769489c27146bdfe1a54938) |
| `babblesim_ext_2G4_phy_v1` | [b0e49ae3dd4d6d0f2286fd1392cee1b5206f5bbc](https://github.com/BabbleSim/ext_2G4_phy_v1/commit/b0e49ae3dd4d6d0f2286fd1392cee1b5206f5bbc) |
| `babblesim_ext_libCryptov1` | [da246018ebe031e4fe4a8228187fb459e9f3b2fa](https://github.com/BabbleSim/ext_libCryptov1/commit/da246018ebe031e4fe4a8228187fb459e9f3b2fa) |
| `bsim` | [0673623452f0a3cb50b7563c32ac7683304cb6fc](https://github.com/zephyrproject-rtos/babblesim-manifest/commit/0673623452f0a3cb50b7563c32ac7683304cb6fc) |


<a id="external-projects-modules"></a>
<a id="west-external-projects"></a>

## 2.4\_外部项目与模块（External Projects/Modules）

以下项目属于外部项目，不直接导入默认清单。使用它们时，需要在自己的清单文件中声明相应项目。参见[清单导入](../west/P013_west清单文件.md#west-manifest-import)，了解如何在继承Zephyr west.yml中必需模块的同时加入这些项目。

向此目录贡献新的外部模块时，使用[专用模板文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/develop/manifest/external/external.rst.tmpl)。

- [Arduino核心API（Arduino Core API）](../external_modules/P013_Arduino核心API.md)
- [CANnectivity_USB转CAN固件（CANnectivity USB to CAN adapter firmware）](../external_modules/P001_CANnectivity_USB转CAN固件.md)
- [CANopenNode协议栈（CANopenNode Protocol Stack）](../external_modules/P002_CANopenNode协议栈.md)
- [上下文中心运行时CHRE（Context Hub Runtime Environment (CHRE)）](../external_modules/P014_上下文中心运行时CHRE.md)
- [CLUTGen标定查找表生成器（CLUTGen）](../external_modules/P015_CLUTGen标定查找表生成器.md)
- [设备树Shell_DTSh（DTSh）](../external_modules/P003_设备树Shell_DTSh.md)
- [Edge_Impulse_SDK（Edge Impulse SDK for Zephyr）](../external_modules/P016_Edge_Impulse_SDK.md)
- [emlearn机器学习（emlearn）](../external_modules/P017_emlearn机器学习.md)
- [ESP串口烧录器（ESP Serial Flasher）](../external_modules/P018_ESP串口烧录器.md)
- [ExecuTorch（ExecuTorch）](../external_modules/P019_ExecuTorch.md)
- [Greybus（Greybus）](../external_modules/P020_Greybus.md)
- [grvl图形库（grvl）](../external_modules/P021_grvl图形库.md)
- [立方星空间协议libcsp（libcsp (Cubesat Space Protocol)）](../external_modules/P022_立方星空间协议libcsp.md)
- [工业IO库libiio（libiio）](../external_modules/P023_工业IO库libiio.md)
- [libmpix图像处理（libmpix）](../external_modules/P024_libmpix图像处理.md)
- [LuDLC数据链路协议（LuDLC）](../external_modules/P025_LuDLC数据链路协议.md)
- [LZ4压缩（LZ4 - Extremely fast compression）](../external_modules/P004_LZ4压缩.md)
- [Memfault固件SDK（memfault-firmware-sdk）](../external_modules/P006_Memfault固件SDK.md)
- [Mender_MCU客户端（mender-mcu）](../external_modules/P007_Mender_MCU客户端.md)
- [Requests_HTTP客户端（requests）](../external_modules/P005_Requests_HTTP客户端.md)
- [IEC60730_B类安全测试（IEC 60730 Class B Safety Test Subsystem）](../external_modules/P012_IEC60730_B类安全测试.md)
- [Thrift（Thrift）](../external_modules/P026_Thrift.md)
- [WebAssembly微运行时WAMR（WebAssembly Micro Runtime (WAMR)）](../external_modules/P027_WebAssembly微运行时WAMR.md)
- [wolfMQTT（wolfMQTT）](../external_modules/P009_wolfMQTT.md)
- [wolfSSH（wolfSSH）](../external_modules/P010_wolfSSH.md)
- [wolfSSL（wolfSSL）](../external_modules/P008_wolfSSL.md)
- [wolfTPM（wolfTPM）](../external_modules/P011_wolfTPM.md)
- [Xedge（Xedge）](../external_modules/P028_Xedge.md)
- [zenoh_pico（zenoh-pico）](../external_modules/P029_zenoh_pico.md)
- [Zephelin性能分析（Zephelin）](../external_modules/P030_Zephelin性能分析.md)
- [Zephyr科学计算库（Zephyr Scientific Library (zscilib)）](../external_modules/P031_Zephyr科学计算库.md)
- [ZView运行时可视化（ZView）](../external_modules/P032_ZView运行时可视化.md)


> 译注——阅读边界：以上32个链接指向Zephyr官网对应介绍页的本地译文，保留各组件独立许可和接入前提。收录为外部项目不等于已经安装，也不等于目标板已支持或验证相应功能。


对应官方文档源码：[doc/develop/manifest/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/index.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：模块与外部项目](P001_模块与外部项目.md) · [本模块主线目录](../reading/modules.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_模块与外部项目.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
