---
id: learning.zephyr-docs.boards-ti.page-13
title: MCU SDK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-mcuplus-sdk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mcu-sdk"></a>

# 第13章\_MCU+ SDK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-mcuplus-sdk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="setup"></a>

## 设置（Setup）

以下步骤反映文档编写时的流程，未来可能变化。目标环境为Linux，并假定已安装python3及openssl等基础工具。

构建前需安装TI MCU+ SDK。请按mcupsdk-core [GitHub仓库](https://github.com/TexasInstruments/mcupsdk-core)中的步骤操作，包括使用west克隆仓库。建议另建Python虚拟环境（venv），因为MCU+ SDK的Python依赖可能与Zephyr冲突。若想少克隆一些仓库，可将west init命令中的all/dev.yml替换为am243x/dev.yml。

还需执行“Downloading And Installing Dependencies”下载及安装依赖章节，但应将命令中的全部am263x替换为am243x。若不需要Doxygen或CCS，可向安装脚本传入--skip_doxygen=true及--skip_ccs=true。若提示某脚本无法执行，请用chmod +x <path>添加执行权限，然后重新运行download_components.sh。

注意（Attention）

请记录工具与mcu_plus_sdk的安装位置。后文以$TI_TOOLS表示download_components.sh使用的工具安装目录，以$MCUPSDK表示运行west init的mcu_plus_sdk目录。建议设置为环境变量，但文件内的占位符仍须按实际位置替换。

注意（Note）

安装MCU+ SDK通常需要执行以下命令或对应调整后的命令：

```text
python3 -m venv .venv
source .venv/bin/activate
pip3 install west
west init -m https://github.com/TexasInstruments/mcupsdk-manifests.git --mr mcupsdk_west --mf am243x/dev.yml
west update
./mcupsdk_setup/am243x/download_components.sh --skip_doxygen=true --skip_ccs=true
```

脚本成功后进入$MCUPSDK，编辑source/drivers/bootloader/bootloader.c，使Bootloader_runCpu中的entryPoint无条件设为0。这是由Zephyr当前镜像构建方式决定的。

随后使用以下命令构建内部库：

```text
make gen-buildfiles DEVICE=am243x PROFILE=release
make libs DEVICE=am243x PROFILE=release
```

若遇到编译错误，需要修复。可能涉及更改参数类型、从Makefile移除缺失的源文件，或从TI在线参考资料下载缺失的头文件。

<a id="building-mcu-sdk-sbls"></a>

## 构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）

SBL示例位于examples/drivers/boot/<example>/$Z_MCUPSDK_BOARD/r5fss0-0_nortos目录。

在$MCUPSDK目录运行make -C examples/drivers/boot/<example>/$Z_MCUPSDK_BOARD/r5fss0-0_nortos/ti-arm-clang/ DEVICE=am243x PROFILE=release即可构建示例。虽然存在sbl_prebuilt目录，但原文编写时该目录为空，只在构建SBL时才会填入内容。

建议根据用途按需构建以下SBL：

`sbl_null`

通过Code Composer Studio集成开发环境（CCS IDE）直接加载Zephyr .elf的引导加载器。易于使用，建议在开发期间从闪存启动它。

`sbl_uart`

通过UART启动RPRC格式固件文件的引导加载器。开发期间建议从UART启动，可避免反复切换UART及OSPI启动模式。

`sbl_ospi`

从闪存加载RPRC格式固件的引导加载器。需要断电后保留启动能力时推荐使用，在闪存偏移0x80000处寻找RPRC镜像。

`sbl_uart_uniflash`

可在RBL之后启动的应用，通常通过UART加载；它经UART接收数据并写入闪存。

更多SBL见[TI MCU+ SDK启动流程文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/BOOTFLOW_GUIDE.html)。

<a id="flashing-data-into-external-flash-with-the-mcu-sdk"></a>

## 使用MCU+ SDK向外部闪存写入数据

向外部闪存写入数据时，先构建sbl_uart_uniflash示例，将生成的sbl_uart_uniflash.release.hs_fs.tiimage复制到工作目录，然后创建配置文件，将$FLASH_OFFSET及$FLASH_FILE分别替换为目标闪存偏移及待写入文件。

注意（Note）

$FLASH_OFFSET应采用0x80000这样的十六进制地址。

注意（Note）

可在不重启的情况下向不同位置写入多个文件，只需复制最后一行并调整文件及闪存偏移。

```text
--flash-writer=sbl_uart_uniflash.release.hs_fs.tiimage
--operation=flash-phy-tuning-data
--file=$FLASH_FILE --operation=flash --flash-offset=$FLASH_OFFSET
```

随后运行python3 uart_uniflash.py -p /dev/ttyUSB0 --cfg=<path-to-the-config-file>。根据连接设备可能需要调整/dev/ttyUSB0。更多说明见[TI MCU+ SDK烧录文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_FLASH.html)。

<a id="creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf"></a>

## 将Zephyr ELF转换为SBL可启动的RPRC镜像

将Zephyr ELF转换为sbl_uart、sbl_ospi等SBL可启动的RPRC文件需要执行多条命令。下面代码块假设zephyr.elf位于当前工作目录；根据固件目标核调整BOOTIMAGE_CORE_ID。

```text
export BOOTIMAGE_CORE_ID_r5fss0-0=4
export BOOTIMAGE_CORE_ID_m4=14
# set CORE_ID as per your target core
export BOOTIMAGE_CORE_ID=${BOOTIMAGE_CORE_ID_desired-core}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/out2rprc/elf2rprc.js ./zephyr.elf
$MCUPSDK/tools/boot/xipGen/xipGen.out -i ./zephyr.rprc -o ./zephyr.rprc_out -x ./zephyr.rprc_out_xip --flash-start-addr 0x60000000
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage ./zephyr.rprc_out@${BOOTIMAGE_CORE_ID}
$TI_TOOLS/sysconfig_1.21.2/nodejs/node $MCUPSDK/tools/boot/multicoreImageGen/multicoreImageGen.js --devID 55 --out ./zephyr.appimage_xip ./zephyr.rprc_out_xip@${BOOTIMAGE_CORE_ID}
python3 $MCUPSDK/source/security/security_common/tools/boot/signing/appimage_x509_cert_gen.py --bin ./zephyr.appimage --authtype 1 --key $MCUPSDK/source/security/security_common/tools/boot/signing/app_degenerateKey.pem --output ./zephyr.appimage.hs_fs
```

结果文件为当前工作目录中的zephyr.appimage.hs_fs，采用SBL能够识别的TI RPRC格式。格式说明见[TI MCU+ SDK启动工具文档](https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am64x/TOOLS_BOOT.html)。

<a id="full-bootflow-examples"></a>

## 完整启动流程示例（Full Bootflow Examples）

下面归纳各启动方式所需步骤。

<a id="tab-0-0-0"></a>

<a id="tab-0-0-1"></a>

<a id="tab-0-0-2"></a>

<a id="panel-0-0-0"></a>

**通过调试器启动（Debugger Booting）**

通过调试器启动时，先按“构建MCU+ SDK的SBL”构建sbl_uart_uniflash及sbl_null，再将开发板切换到UART启动模式，按“[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)”将sbl_null.release.hs_fs.tiimage写到0x0。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)）

随后切换到OSPI启动模式，通过Code Composer Studio调试器直接向所需核加载Zephyr ELF文件。

<a id="panel-0-0-1"></a>

**UART启动**

通过UART启动镜像时，先按“构建MCU+ SDK的SBL”构建sbl_uart，并将开发板切换到UART启动模式。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)）

随后按“[将Zephyr ELF转换为SBL可启动的RPRC镜像](#creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf)”进行转换，并运行python3 $MCUPSDK/tools/boot/uart_bootloader.py -p /dev/ttyUSB0 --bootloader=sbl_uart.release.hs_fs.tiimage --file=zephyr.appimage.hs_fs。

<a id="panel-0-0-2"></a>

**OSPI启动**

通过OSPI启动镜像时，先按“构建MCU+ SDK的SBL”构建sbl_uart_uniflash及sbl_ospi，再将开发板切换到UART启动模式，按外部闪存烧录步骤将sbl_ospi.release.hs_fs.tiimage写到0x0；此操作只需执行一次。（[构建MCU+ SDK的SBL（Building MCU+ SDK SBLs）](#building-mcu-sdk-sbls)；[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)）

此后每次新构建Zephyr固件，都需按RPRC转换步骤转换ELF，并按外部闪存烧录步骤写入0x80000。随后切换到OSPI启动模式即可运行。（[将Zephyr ELF转换为SBL可启动的RPRC镜像](#creating-a-sbl-bootable-rprc-image-from-a-zephyr-elf)；[使用MCU+ SDK向外部闪存写入数据](#flashing-data-into-external-flash-with-the-mcu-sdk)）

## 译注

MCU+ SDK步骤假定Linux环境，推荐独立Python虚拟环境。保留Bootloader_runCpu的entryPoint置0、SBL构建、RPRC转换以及0x0／0x80000写入位置。所有工具路径使用变量或占位符，未加入本机仓库位置。

---

[上一章](P012_AM64x_AM243x_features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Texas_Instruments.md)
