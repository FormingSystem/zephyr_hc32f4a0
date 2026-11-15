---
id: learning.zephyr-docs.memory-retention-reference.page-1
title: NVMEM公共头文件源码
kind: reference
status: maintained
domains: [zephyr, storage, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nvmem_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_NVMEM公共头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nvmem_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](../storage/P020_NVMEM公共头文件.md)和[公共API](../storage/P013_NVMEM接口参考.md)。

## 1.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00037"></a>
<a id="foldopen00096"></a>
<a id="foldopen00189"></a>
<a id="foldopen00208"></a>
<a id="foldopen00293"></a>
<a id="foldopen00311"></a>
<a id="foldopen00363"></a>
<a id="foldopen00375"></a>
<a id="foldopen00389"></a>
<a id="foldopen00411"></a>
<a id="foldopen00433"></a>
<a id="foldopen00455"></a>
<a id="foldopen00477"></a>
<a id="foldopen00499"></a>
<a id="foldopen00521"></a>
<a id="foldopen00543"></a>
<a id="foldopen00565"></a>
<a id="foldopen00583"></a>
<a id="foldopen00601"></a>
<a id="foldopen00619"></a>
<a id="foldopen00637"></a>
<a id="foldopen00655"></a>
<a id="foldopen00673"></a>
<a id="foldopen00691"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_2nvmem_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__nvmem__interface_html_ga1c119e9ad5817f47a6b99aaebc492da8"></a>
<a id="agroup__nvmem__interface_html_ga2ff30423cff4e064ab22cc13ff2fd60a"></a>
<a id="agroup__nvmem__interface_html_ga377f8afd53d1d84e630de96a3620c13a"></a>
<a id="agroup__nvmem__interface_html_ga3929245cba736565c5d7f746b09147a4"></a>
<a id="agroup__nvmem__interface_html_ga405e1697ca3ff9c8f33a3fea5dc8ffdb"></a>
<a id="agroup__nvmem__interface_html_ga43e38af86b79d9ae5d9933e95fbbb134"></a>
<a id="agroup__nvmem__interface_html_ga495e06601cfc7d7f41d3b16a58476b67"></a>
<a id="agroup__nvmem__interface_html_ga4fac111617d3a2a2affab26d239c91ea"></a>
<a id="agroup__nvmem__interface_html_ga5846faeb71b80da68044229de943833b"></a>
<a id="agroup__nvmem__interface_html_ga5db94733cecfd4b46dd87ee07128d58d"></a>
<a id="agroup__nvmem__interface_html_ga614cac8acc913cb2f7b62c2f0d625421"></a>
<a id="agroup__nvmem__interface_html_ga8d0acdfeb984292616d0a5c8b90c37be"></a>
<a id="agroup__nvmem__interface_html_ga8e4eca68269a125baa5ae1bd6813a50a"></a>
<a id="agroup__nvmem__interface_html_gabf0dc8224abaeec54537c84b4bf0aa9b"></a>
<a id="agroup__nvmem__interface_html_gac882709f9a2f8dcd4f48119cc73db3bd"></a>
<a id="agroup__nvmem__interface_html_gac8abd20a158e3c304c73d6cb7e8cc50a"></a>
<a id="agroup__nvmem__interface_html_gacce8148eeac974048659efea2be2d9bf"></a>
<a id="agroup__nvmem__interface_html_gae0974ff5106a37609d218340aad758ff"></a>
<a id="agroup__nvmem__interface_html_gaef749ffc4b49e2e37b489fab2d8fa6b4"></a>
<a id="agroup__nvmem__interface_html_gaf61422106876ef0995d0e5e6ebda6bd5"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructnvmem__cell_html"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2byteorder_8h_html_a21f25ff68591217034f3414594425286"></a>
<a id="asys_2byteorder_8h_html_a3e0d2e4e85249497011f5f9ea0d2987c"></a>
<a id="asys_2byteorder_8h_html_a4db31229c7a8a80dace3870664b6442d"></a>
<a id="asys_2byteorder_8h_html_a5c2c537b960a29bdd29133f902a67f6a"></a>
<a id="asys_2byteorder_8h_html_a601c3cefbdfd8befa336339a87fd70fd"></a>
<a id="asys_2byteorder_8h_html_a678b08370e157ce5eb7117832aa86408"></a>
<a id="asys_2byteorder_8h_html_a68df8f14dfc0d8715d16ac87dd4c73d2"></a>
<a id="asys_2byteorder_8h_html_a7d89d4b4b278fefa3e65fc6c3894a70c"></a>
<a id="asys_2byteorder_8h_html_a91fae25b12126c2b35d240f56866184d"></a>
<a id="asys_2byteorder_8h_html_aa6950654cc7fd67ab4f83235da59665a"></a>
<a id="asys_2byteorder_8h_html_aa7422f922db351d2da1d52195d43b8a4"></a>
<a id="asys_2byteorder_8h_html_abe8d617e8a5469c303a512fe94a55443"></a>
<a id="asys_2byteorder_8h_html_acf0fa9761998529910e022b80126ff6b"></a>
<a id="asys_2byteorder_8h_html_ad8e00ff5c0b9e394291936d1a570c215"></a>
<a id="asys_2byteorder_8h_html_af8f30219c861bb07d097374204d386dd"></a>
<a id="asys_2byteorder_8h_html_aff60d0dcda6a48df4ea248f898a92de0"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2025 Basalte bv
<a id="l00003"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00004"></a> */
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_NVMEM_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_NVMEM_H_
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>#include &lt;sys/types.h&gt;
<a id="l00025"></a>#include &lt;zephyr/device.h&gt;
<a id="l00026"></a>#include &lt;zephyr/devicetree.h&gt;
<a id="l00027"></a>#include &lt;zephyr/devicetree/nvmem.h&gt;
<a id="l00028"></a>#include &lt;zephyr/sys/byteorder.h&gt;
<a id="l00029"></a>
<a id="l00030"></a>#ifdef __cplusplus
<a id="l00031"></a>extern "C" {
<a id="l00032"></a>#endif
<a id="l00033"></a>
<a id="l00037"></a>struct nvmem_cell {
<a id="l00038"></a>        /* @cond INTERNAL_HIDDEN */
<a id="l00039"></a>
<a id="l00041"></a>        const struct device *dev;
<a id="l00043"></a>        off_t offset;
<a id="l00045"></a>        size_t size;
<a id="l00047"></a>        bool read_only;
<a id="l00048"></a>
<a id="l00049"></a>        /* @endcond */
<a id="l00050"></a>};
<a id="l00051"></a>
<a id="l00096"></a>#define NVMEM_CELL_INIT(node_id)                                                                   \
<a id="l00097"></a>        {                                                                                          \
<a id="l00098"></a>                .dev = DEVICE_DT_GET(DT_MTD_FROM_NVMEM_CELL(node_id)),                             \
<a id="l00099"></a>                .offset = DT_REG_ADDR(node_id),                                                    \
<a id="l00100"></a>                .size = DT_REG_SIZE(node_id),                                                      \
<a id="l00101"></a>                .read_only = DT_PROP(node_id, read_only),                                          \
<a id="l00102"></a>        }
<a id="l00103"></a>
<a id="l00155"></a>#define NVMEM_CELL_GET_BY_NAME(node_id, name) NVMEM_CELL_INIT(DT_NVMEM_CELL_BY_NAME(node_id, name))
<a id="l00156"></a>
<a id="l00169"></a>#define NVMEM_CELL_INST_GET_BY_NAME(inst, name) NVMEM_CELL_GET_BY_NAME(DT_DRV_INST(inst), name)
<a id="l00170"></a>
<a id="l00189"></a>#define NVMEM_CELL_GET_BY_NAME_OR(node_id, name, default_value)                                    \
<a id="l00190"></a>        COND_CODE_1(DT_PROP_HAS_NAME(node_id, nvmem_cells, name),                                  \
<a id="l00191"></a>                    (NVMEM_CELL_GET_BY_NAME(node_id, name)),                                       \
<a id="l00192"></a>                    (default_value))
<a id="l00193"></a>
<a id="l00208"></a>#define NVMEM_CELL_INST_GET_BY_NAME_OR(inst, name, default_value)                                  \
<a id="l00209"></a>        NVMEM_CELL_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
<a id="l00210"></a>
<a id="l00261"></a>#define NVMEM_CELL_GET_BY_IDX(node_id, idx) NVMEM_CELL_INIT(DT_NVMEM_CELL_BY_IDX(node_id, idx))
<a id="l00262"></a>
<a id="l00274"></a>#define NVMEM_CELL_INST_GET_BY_IDX(inst, idx) NVMEM_CELL_GET_BY_IDX(DT_DRV_INST(inst), idx)
<a id="l00275"></a>
<a id="l00293"></a>#define NVMEM_CELL_GET_BY_IDX_OR(node_id, idx, default_value)                                      \
<a id="l00294"></a>        COND_CODE_1(DT_PROP_HAS_IDX(node_id, nvmem_cells, idx),                                    \
<a id="l00295"></a>                    (NVMEM_CELL_GET_BY_IDX(node_id, idx)),                                         \
<a id="l00296"></a>                    (default_value))
<a id="l00297"></a>
<a id="l00311"></a>#define NVMEM_CELL_INST_GET_BY_IDX_OR(inst, idx, default_value)                                    \
<a id="l00312"></a>        NVMEM_CELL_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
<a id="l00313"></a>
<a id="l00332"></a>int nvmem_cell_read(const struct nvmem_cell *cell, void *data, off_t off, size_t len);
<a id="l00333"></a>
<a id="l00354"></a>int nvmem_cell_write(const struct nvmem_cell *cell, const void *data, off_t off, size_t len);
<a id="l00355"></a>
<a id="l00363"></a>static inline bool nvmem_cell_is_ready(const struct nvmem_cell *cell)
<a id="l00364"></a>{
<a id="l00365"></a>        return cell != NULL &amp;&amp; device_is_ready(cell-&gt;dev);
<a id="l00366"></a>}
<a id="l00367"></a>
<a id="l00375"></a>static inline bool nvmem_cell_is_read_only(const struct nvmem_cell *cell)
<a id="l00376"></a>{
<a id="l00377"></a>        return cell-&gt;read_only;
<a id="l00378"></a>}
<a id="l00379"></a>
<a id="l00389"></a>static inline int nvmem_cell_read_le16(const struct nvmem_cell *cell, uint16_t *val, off_t off)
<a id="l00390"></a>{
<a id="l00391"></a>        uint8_t buf[sizeof(uint16_t)];
<a id="l00392"></a>        int ret;
<a id="l00393"></a>
<a id="l00394"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00395"></a>        if (ret == 0) {
<a id="l00396"></a>                *val = sys_get_le16(buf);
<a id="l00397"></a>        }
<a id="l00398"></a>
<a id="l00399"></a>        return ret;
<a id="l00400"></a>}
<a id="l00401"></a>
<a id="l00411"></a>static inline int nvmem_cell_read_be16(const struct nvmem_cell *cell, uint16_t *val, off_t off)
<a id="l00412"></a>{
<a id="l00413"></a>        uint8_t buf[sizeof(uint16_t)];
<a id="l00414"></a>        int ret;
<a id="l00415"></a>
<a id="l00416"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00417"></a>        if (ret == 0) {
<a id="l00418"></a>                *val = sys_get_be16(buf);
<a id="l00419"></a>        }
<a id="l00420"></a>
<a id="l00421"></a>        return ret;
<a id="l00422"></a>}
<a id="l00423"></a>
<a id="l00433"></a>static inline int nvmem_cell_read_le32(const struct nvmem_cell *cell, uint32_t *val, off_t off)
<a id="l00434"></a>{
<a id="l00435"></a>        uint8_t buf[sizeof(uint32_t)];
<a id="l00436"></a>        int ret;
<a id="l00437"></a>
<a id="l00438"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00439"></a>        if (ret == 0) {
<a id="l00440"></a>                *val = sys_get_le32(buf);
<a id="l00441"></a>        }
<a id="l00442"></a>
<a id="l00443"></a>        return ret;
<a id="l00444"></a>}
<a id="l00445"></a>
<a id="l00455"></a>static inline int nvmem_cell_read_be32(const struct nvmem_cell *cell, uint32_t *val, off_t off)
<a id="l00456"></a>{
<a id="l00457"></a>        uint8_t buf[sizeof(uint32_t)];
<a id="l00458"></a>        int ret;
<a id="l00459"></a>
<a id="l00460"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00461"></a>        if (ret == 0) {
<a id="l00462"></a>                *val = sys_get_be32(buf);
<a id="l00463"></a>        }
<a id="l00464"></a>
<a id="l00465"></a>        return ret;
<a id="l00466"></a>}
<a id="l00467"></a>
<a id="l00477"></a>static inline int nvmem_cell_read_le48(const struct nvmem_cell *cell, uint64_t *val, off_t off)
<a id="l00478"></a>{
<a id="l00479"></a>        uint8_t buf[6];
<a id="l00480"></a>        int ret;
<a id="l00481"></a>
<a id="l00482"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00483"></a>        if (ret == 0) {
<a id="l00484"></a>                *val = sys_get_le48(buf);
<a id="l00485"></a>        }
<a id="l00486"></a>
<a id="l00487"></a>        return ret;
<a id="l00488"></a>}
<a id="l00489"></a>
<a id="l00499"></a>static inline int nvmem_cell_read_be48(const struct nvmem_cell *cell, uint64_t *val, off_t off)
<a id="l00500"></a>{
<a id="l00501"></a>        uint8_t buf[6];
<a id="l00502"></a>        int ret;
<a id="l00503"></a>
<a id="l00504"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00505"></a>        if (ret == 0) {
<a id="l00506"></a>                *val = sys_get_be48(buf);
<a id="l00507"></a>        }
<a id="l00508"></a>
<a id="l00509"></a>        return ret;
<a id="l00510"></a>}
<a id="l00511"></a>
<a id="l00521"></a>static inline int nvmem_cell_read_le64(const struct nvmem_cell *cell, uint64_t *val, off_t off)
<a id="l00522"></a>{
<a id="l00523"></a>        uint8_t buf[sizeof(uint64_t)];
<a id="l00524"></a>        int ret;
<a id="l00525"></a>
<a id="l00526"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00527"></a>        if (ret == 0) {
<a id="l00528"></a>                *val = sys_get_le64(buf);
<a id="l00529"></a>        }
<a id="l00530"></a>
<a id="l00531"></a>        return ret;
<a id="l00532"></a>}
<a id="l00533"></a>
<a id="l00543"></a>static inline int nvmem_cell_read_be64(const struct nvmem_cell *cell, uint64_t *val, off_t off)
<a id="l00544"></a>{
<a id="l00545"></a>        uint8_t buf[sizeof(uint64_t)];
<a id="l00546"></a>        int ret;
<a id="l00547"></a>
<a id="l00548"></a>        ret = nvmem_cell_read(cell, buf, off, sizeof(buf));
<a id="l00549"></a>        if (ret == 0) {
<a id="l00550"></a>                *val = sys_get_be64(buf);
<a id="l00551"></a>        }
<a id="l00552"></a>
<a id="l00553"></a>        return ret;
<a id="l00554"></a>}
<a id="l00555"></a>
<a id="l00565"></a>static inline int nvmem_cell_write_le16(const struct nvmem_cell *cell, uint16_t val, off_t off)
<a id="l00566"></a>{
<a id="l00567"></a>        uint8_t buf[sizeof(uint16_t)];
<a id="l00568"></a>
<a id="l00569"></a>        sys_put_le16(val, buf);
<a id="l00570"></a>
<a id="l00571"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00572"></a>}
<a id="l00573"></a>
<a id="l00583"></a>static inline int nvmem_cell_write_be16(const struct nvmem_cell *cell, uint16_t val, off_t off)
<a id="l00584"></a>{
<a id="l00585"></a>        uint8_t buf[sizeof(uint16_t)];
<a id="l00586"></a>
<a id="l00587"></a>        sys_put_be16(val, buf);
<a id="l00588"></a>
<a id="l00589"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00590"></a>}
<a id="l00591"></a>
<a id="l00601"></a>static inline int nvmem_cell_write_le32(const struct nvmem_cell *cell, uint32_t val, off_t off)
<a id="l00602"></a>{
<a id="l00603"></a>        uint8_t buf[sizeof(uint32_t)];
<a id="l00604"></a>
<a id="l00605"></a>        sys_put_le32(val, buf);
<a id="l00606"></a>
<a id="l00607"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00608"></a>}
<a id="l00609"></a>
<a id="l00619"></a>static inline int nvmem_cell_write_be32(const struct nvmem_cell *cell, uint32_t val, off_t off)
<a id="l00620"></a>{
<a id="l00621"></a>        uint8_t buf[sizeof(uint32_t)];
<a id="l00622"></a>
<a id="l00623"></a>        sys_put_be32(val, buf);
<a id="l00624"></a>
<a id="l00625"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00626"></a>}
<a id="l00627"></a>
<a id="l00637"></a>static inline int nvmem_cell_write_le48(const struct nvmem_cell *cell, uint64_t val, off_t off)
<a id="l00638"></a>{
<a id="l00639"></a>        uint8_t buf[6];
<a id="l00640"></a>
<a id="l00641"></a>        sys_put_le48(val, buf);
<a id="l00642"></a>
<a id="l00643"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00644"></a>}
<a id="l00645"></a>
<a id="l00655"></a>static inline int nvmem_cell_write_be48(const struct nvmem_cell *cell, uint64_t val, off_t off)
<a id="l00656"></a>{
<a id="l00657"></a>        uint8_t buf[6];
<a id="l00658"></a>
<a id="l00659"></a>        sys_put_be48(val, buf);
<a id="l00660"></a>
<a id="l00661"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00662"></a>}
<a id="l00663"></a>
<a id="l00673"></a>static inline int nvmem_cell_write_le64(const struct nvmem_cell *cell, uint64_t val, off_t off)
<a id="l00674"></a>{
<a id="l00675"></a>        uint8_t buf[sizeof(uint64_t)];
<a id="l00676"></a>
<a id="l00677"></a>        sys_put_le64(val, buf);
<a id="l00678"></a>
<a id="l00679"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00680"></a>}
<a id="l00681"></a>
<a id="l00691"></a>static inline int nvmem_cell_write_be64(const struct nvmem_cell *cell, uint64_t val, off_t off)
<a id="l00692"></a>{
<a id="l00693"></a>        uint8_t buf[sizeof(uint64_t)];
<a id="l00694"></a>
<a id="l00695"></a>        sys_put_be64(val, buf);
<a id="l00696"></a>
<a id="l00697"></a>        return nvmem_cell_write(cell, buf, off, sizeof(buf));
<a id="l00698"></a>}
<a id="l00699"></a>
<a id="l00700"></a>#ifdef __cplusplus
<a id="l00701"></a>}
<a id="l00702"></a>#endif
<a id="l00703"></a>
<a id="l00707"></a>
<a id="l00708"></a>#endif /* ZEPHYR_INCLUDE_NVMEM_H_ */
</code></pre>

## 1.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2025 Basalte bv。Apache-2.0许可证原文保留。

2. 开始Doxygen内部隐藏区域（INTERNAL_HIDDEN）。

3. 结束Doxygen条件展示区域。

4. 结束头文件包含保护ZEPHYR_INCLUDE_NVMEM_H_。

## 1.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API和宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `nvmem.h`

非易失性存储器（Non-Volatile Memory，NVMEM）的公共设备树（Devicetree）头文件。

符号定位：[nvmem.h](P002_NVMEM设备树头文件参考.md)。

### `devicetree.h`

设备树（Devicetree）主头文件。

符号定位：[devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)。

### `device_is_ready`

```c
bool device_is_ready(const struct device *dev)
```

确认设备已就绪，可以使用。

符号定位：[device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。

### `nvmem_cell_write_be48`

```c
static int nvmem_cell_write_be48(const struct nvmem_cell *cell, uint64_t val, off_t off)
```

向NVMEM数据单元写入大端（Big Endian）48位值。

定义位置（Definition）：nvmem.h:655。

符号定位：[nvmem_cell_write_be48](../storage/P013_NVMEM接口参考.md#ga1c119e9ad5817f47a6b99aaebc492da8)。

### `nvmem_cell_write_le32`

```c
static int nvmem_cell_write_le32(const struct nvmem_cell *cell, uint32_t val, off_t off)
```

向NVMEM数据单元写入小端（Little Endian）32位值。

定义位置（Definition）：nvmem.h:601。

符号定位：[nvmem_cell_write_le32](../storage/P013_NVMEM接口参考.md#ga2ff30423cff4e064ab22cc13ff2fd60a)。

### `nvmem_cell_write_le48`

```c
static int nvmem_cell_write_le48(const struct nvmem_cell *cell, uint64_t val, off_t off)
```

向NVMEM数据单元写入小端（Little Endian）48位值。

定义位置（Definition）：nvmem.h:637。

符号定位：[nvmem_cell_write_le48](../storage/P013_NVMEM接口参考.md#ga377f8afd53d1d84e630de96a3620c13a)。

### `nvmem_cell_read_le32`

```c
static int nvmem_cell_read_le32(const struct nvmem_cell *cell, uint32_t *val, off_t off)
```

从NVMEM数据单元读取小端（Little Endian）32位值。

定义位置（Definition）：nvmem.h:433。

符号定位：[nvmem_cell_read_le32](../storage/P013_NVMEM接口参考.md#ga3929245cba736565c5d7f746b09147a4)。

### `nvmem_cell_read_le48`

```c
static int nvmem_cell_read_le48(const struct nvmem_cell *cell, uint64_t *val, off_t off)
```

从NVMEM数据单元读取小端（Little Endian）48位值。

定义位置（Definition）：nvmem.h:477。

符号定位：[nvmem_cell_read_le48](../storage/P013_NVMEM接口参考.md#ga405e1697ca3ff9c8f33a3fea5dc8ffdb)。

### `nvmem_cell_write_be16`

```c
static int nvmem_cell_write_be16(const struct nvmem_cell *cell, uint16_t val, off_t off)
```

向NVMEM数据单元写入大端（Big Endian）16位值。

定义位置（Definition）：nvmem.h:583。

符号定位：[nvmem_cell_write_be16](../storage/P013_NVMEM接口参考.md#ga43e38af86b79d9ae5d9933e95fbbb134)。

### `nvmem_cell_write_be64`

```c
static int nvmem_cell_write_be64(const struct nvmem_cell *cell, uint64_t val, off_t off)
```

向NVMEM数据单元写入大端（Big Endian）64位值。

定义位置（Definition）：nvmem.h:691。

符号定位：[nvmem_cell_write_be64](../storage/P013_NVMEM接口参考.md#ga495e06601cfc7d7f41d3b16a58476b67)。

### `nvmem_cell_read_le16`

```c
static int nvmem_cell_read_le16(const struct nvmem_cell *cell, uint16_t *val, off_t off)
```

从NVMEM数据单元读取小端（Little Endian）16位值。

定义位置（Definition）：nvmem.h:389。

符号定位：[nvmem_cell_read_le16](../storage/P013_NVMEM接口参考.md#ga4fac111617d3a2a2affab26d239c91ea)。

### `nvmem_cell_write_le16`

```c
static int nvmem_cell_write_le16(const struct nvmem_cell *cell, uint16_t val, off_t off)
```

向NVMEM数据单元写入小端（Little Endian）16位值。

定义位置（Definition）：nvmem.h:565。

符号定位：[nvmem_cell_write_le16](../storage/P013_NVMEM接口参考.md#ga5846faeb71b80da68044229de943833b)。

### `nvmem_cell_read`

```c
int nvmem_cell_read(const struct nvmem_cell *cell, void *data, off_t off, size_t len)
```

从NVMEM数据单元读取数据。

符号定位：[nvmem_cell_read](../storage/P013_NVMEM接口参考.md#ga5db94733cecfd4b46dd87ee07128d58d)。

### `nvmem_cell_is_ready`

```c
static bool nvmem_cell_is_ready(const struct nvmem_cell *cell)
```

检查NVMEM数据单元是否就绪。

定义位置（Definition）：nvmem.h:363。

符号定位：[nvmem_cell_is_ready](../storage/P013_NVMEM接口参考.md#ga614cac8acc913cb2f7b62c2f0d625421)。

### `nvmem_cell_read_be16`

```c
static int nvmem_cell_read_be16(const struct nvmem_cell *cell, uint16_t *val, off_t off)
```

从NVMEM数据单元读取大端（Big Endian）16位值。

定义位置（Definition）：nvmem.h:411。

符号定位：[nvmem_cell_read_be16](../storage/P013_NVMEM接口参考.md#ga8d0acdfeb984292616d0a5c8b90c37be)。

### `nvmem_cell_write_be32`

```c
static int nvmem_cell_write_be32(const struct nvmem_cell *cell, uint32_t val, off_t off)
```

向NVMEM数据单元写入大端（Big Endian）32位值。

定义位置（Definition）：nvmem.h:619。

符号定位：[nvmem_cell_write_be32](../storage/P013_NVMEM接口参考.md#ga8e4eca68269a125baa5ae1bd6813a50a)。

### `nvmem_cell_read_be64`

```c
static int nvmem_cell_read_be64(const struct nvmem_cell *cell, uint64_t *val, off_t off)
```

从NVMEM数据单元读取大端（Big Endian）64位值。

定义位置（Definition）：nvmem.h:543。

符号定位：[nvmem_cell_read_be64](../storage/P013_NVMEM接口参考.md#gabf0dc8224abaeec54537c84b4bf0aa9b)。

### `nvmem_cell_write_le64`

```c
static int nvmem_cell_write_le64(const struct nvmem_cell *cell, uint64_t val, off_t off)
```

向NVMEM数据单元写入小端（Little Endian）64位值。

定义位置（Definition）：nvmem.h:673。

符号定位：[nvmem_cell_write_le64](../storage/P013_NVMEM接口参考.md#gac882709f9a2f8dcd4f48119cc73db3bd)。

### `nvmem_cell_is_read_only`

```c
static bool nvmem_cell_is_read_only(const struct nvmem_cell *cell)
```

检查NVMEM数据单元是否只读（Read-only）。

定义位置（Definition）：nvmem.h:375。

符号定位：[nvmem_cell_is_read_only](../storage/P013_NVMEM接口参考.md#gac8abd20a158e3c304c73d6cb7e8cc50a)。

### `nvmem_cell_read_be32`

```c
static int nvmem_cell_read_be32(const struct nvmem_cell *cell, uint32_t *val, off_t off)
```

从NVMEM数据单元读取大端（Big Endian）32位值。

定义位置（Definition）：nvmem.h:455。

符号定位：[nvmem_cell_read_be32](../storage/P013_NVMEM接口参考.md#gacce8148eeac974048659efea2be2d9bf)。

### `nvmem_cell_read_be48`

```c
static int nvmem_cell_read_be48(const struct nvmem_cell *cell, uint64_t *val, off_t off)
```

从NVMEM数据单元读取大端（Big Endian）48位值。

定义位置（Definition）：nvmem.h:499。

符号定位：[nvmem_cell_read_be48](../storage/P013_NVMEM接口参考.md#gae0974ff5106a37609d218340aad758ff)。

### `nvmem_cell_write`

```c
int nvmem_cell_write(const struct nvmem_cell *cell, const void *data, off_t off, size_t len)
```

向NVMEM数据单元写入数据。

符号定位：[nvmem_cell_write](../storage/P013_NVMEM接口参考.md#gaef749ffc4b49e2e37b489fab2d8fa6b4)。

### `nvmem_cell_read_le64`

```c
static int nvmem_cell_read_le64(const struct nvmem_cell *cell, uint64_t *val, off_t off)
```

从NVMEM数据单元读取小端（Little Endian）64位值。

定义位置（Definition）：nvmem.h:521。

符号定位：[nvmem_cell_read_le64](../storage/P013_NVMEM接口参考.md#gaf61422106876ef0995d0e5e6ebda6bd5)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)。

### `off_t`

```c
__INTPTR_TYPE__ off_t
```

定义位置（Definition）：types.h:36。

符号定位：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint64_t`

```c
__UINT64_TYPE__ uint64_t
```

定义位置（Definition）：stdint.h:91。

符号定位：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `device`

每个驱动实例的运行时设备结构（Runtime Device Structure，位于ROM中）。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `device::data`

```c
void * data
```

设备实例私有数据（Private Data）的地址。

定义位置（Definition）：device.h:553。

符号定位：[device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)。

### `nvmem_cell`

非易失性存储器（Non-Volatile Memory）数据单元的表示。

定义位置（Definition）：nvmem.h:37。

符号定位：[nvmem_cell](../storage/P019_NVMEM数据单元结构.md)。

### `byteorder.h`

字节序（Byte Order）辅助函数。

符号定位：[byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)。

### `sys_put_be32`

```c
static void sys_put_be32(uint32_t val, uint8_t dst[4])
```

以大端（Big Endian）格式将32位整数写入任意位置。

定义位置（Definition）：byteorder.h:373。

符号定位：[sys_put_be32](../byteorder_reference/P001_系统字节序头文件参考.md#a21f25ff68591217034f3414594425286)。

### `sys_put_be64`

```c
static void sys_put_be64(uint64_t val, uint8_t dst[8])
```

以大端（Big Endian）格式将64位整数写入任意位置。

定义位置（Definition）：byteorder.h:417。

符号定位：[sys_put_be64](../byteorder_reference/P001_系统字节序头文件参考.md#a3e0d2e4e85249497011f5f9ea0d2987c)。

### `sys_get_be32`

```c
static uint32_t sys_get_be32(const uint8_t src[4])
```

读取以大端（Big Endian）格式存储的32位整数。

定义位置（Definition）：byteorder.h:553。

符号定位：[sys_get_be32](../byteorder_reference/P001_系统字节序头文件参考.md#a4db31229c7a8a80dace3870664b6442d)。

### `sys_get_le16`

```c
static uint16_t sys_get_le16(const uint8_t src[2])
```

读取以小端（Little Endian）格式存储的16位整数。

定义位置（Definition）：byteorder.h:613。

符号定位：[sys_get_le16](../byteorder_reference/P001_系统字节序头文件参考.md#a5c2c537b960a29bdd29133f902a67f6a)。

### `sys_get_le48`

```c
static uint64_t sys_get_le48(const uint8_t src[6])
```

读取以小端（Little Endian）格式存储的48位整数。

定义位置（Definition）：byteorder.h:673。

符号定位：[sys_get_le48](../byteorder_reference/P001_系统字节序头文件参考.md#a601c3cefbdfd8befa336339a87fd70fd)。

### `sys_get_le64`

```c
static uint64_t sys_get_le64(const uint8_t src[8])
```

读取以小端（Little Endian）格式存储的64位整数。

定义位置（Definition）：byteorder.h:688。

符号定位：[sys_get_le64](../byteorder_reference/P001_系统字节序头文件参考.md#a678b08370e157ce5eb7117832aa86408)。

### `sys_put_be16`

```c
static void sys_put_be16(uint16_t val, uint8_t dst[2])
```

以大端（Big Endian）格式将16位整数写入任意位置。

定义位置（Definition）：byteorder.h:343。

符号定位：[sys_put_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a68df8f14dfc0d8715d16ac87dd4c73d2)。

### `sys_put_le64`

```c
static void sys_put_le64(uint64_t val, uint8_t dst[8])
```

以小端（Little Endian）格式将64位整数写入任意位置。

定义位置（Definition）：byteorder.h:507。

符号定位：[sys_put_le64](../byteorder_reference/P001_系统字节序头文件参考.md#a7d89d4b4b278fefa3e65fc6c3894a70c)。

### `sys_get_be16`

```c
static uint16_t sys_get_be16(const uint8_t src[2])
```

读取以大端（Big Endian）格式存储的16位整数。

定义位置（Definition）：byteorder.h:523。

符号定位：[sys_get_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a91fae25b12126c2b35d240f56866184d)。

### `sys_put_le48`

```c
static void sys_put_le48(uint64_t val, uint8_t dst[6])
```

以小端（Little Endian）格式将48位整数写入任意位置。

定义位置（Definition）：byteorder.h:492。

符号定位：[sys_put_le48](../byteorder_reference/P001_系统字节序头文件参考.md#aa6950654cc7fd67ab4f83235da59665a)。

### `sys_get_le32`

```c
static uint32_t sys_get_le32(const uint8_t src[4])
```

读取以小端（Little Endian）格式存储的32位整数。

定义位置（Definition）：byteorder.h:643。

符号定位：[sys_get_le32](../byteorder_reference/P001_系统字节序头文件参考.md#aa7422f922db351d2da1d52195d43b8a4)。

### `sys_put_be48`

```c
static void sys_put_be48(uint64_t val, uint8_t dst[6])
```

以大端（Big Endian）格式将48位整数写入任意位置。

定义位置（Definition）：byteorder.h:402。

符号定位：[sys_put_be48](../byteorder_reference/P001_系统字节序头文件参考.md#abe8d617e8a5469c303a512fe94a55443)。

### `sys_get_be48`

```c
static uint64_t sys_get_be48(const uint8_t src[6])
```

读取以大端（Big Endian）格式存储的48位整数。

定义位置（Definition）：byteorder.h:583。

符号定位：[sys_get_be48](../byteorder_reference/P001_系统字节序头文件参考.md#acf0fa9761998529910e022b80126ff6b)。

### `sys_get_be64`

```c
static uint64_t sys_get_be64(const uint8_t src[8])
```

读取以大端（Big Endian）格式存储的64位整数。

定义位置（Definition）：byteorder.h:598。

符号定位：[sys_get_be64](../byteorder_reference/P001_系统字节序头文件参考.md#ad8e00ff5c0b9e394291936d1a570c215)。

### `sys_put_le16`

```c
static void sys_put_le16(uint16_t val, uint8_t dst[2])
```

以小端（Little Endian）格式将16位整数写入任意位置。

定义位置（Definition）：byteorder.h:432。

符号定位：[sys_put_le16](../byteorder_reference/P001_系统字节序头文件参考.md#af8f30219c861bb07d097374204d386dd)。

### `sys_put_le32`

```c
static void sys_put_le32(uint32_t val, uint8_t dst[4])
```

以小端（Little Endian）格式将32位整数写入任意位置。

定义位置（Definition）：byteorder.h:462。

符号定位：[sys_put_le32](../byteorder_reference/P001_系统字节序头文件参考.md#aff60d0dcda6a48df4ea248f898a92de0)。

## 1.4\_源码跟踪译注

> 译注——层次与初始化：NVMEM按数据单元（Cell）描述底层设备、单元偏移、大小和只读属性。NVMEM_CELL_INIT生成结构初始化内容，不分配或复制存储数据；设备由数据单元祖父节点取得。应用应先用nvmem_cell_is_ready检查；它允许cell为NULL并返回false，而nvmem_cell_is_read_only直接解引用cell，要求有效指针。

> 译注——偏移和后端：off相对于数据单元，实际后端偏移为cell->offset+off。nvmem.c按启用的配置和设备API类别分派给BBRAM、EEPROM、Flash或一次性可编程存储器（One-Time Programmable Memory，OTP）；读写支持由不同配置决定。写入前检查read_only，返回-EROFS；未就绪返回-ENODEV，无匹配后端返回-ENXIO。通用写入口不替调用者擦除Flash，也不把OTP编程变成可反复覆盖的RAM写入。

> 译注——范围检查：当前后端用off < 0及cell->size < off + len判断范围，调用者还应保证混合有符号／无符号的加法不溢出，以及cell->offset+off可表示。cell空指针只由断言检查，关闭断言不等于参数会转换成普通错误码；缓冲区必须有效，不能把这些条件视为完整的防御性校验。

> 译注——整数序列化：16／32／64位辅助函数处理2／4／8字节；48位辅助函数使用6字节缓冲区和uint64_t承载数值。读取仅在底层返回0后写入*val，失败时不会用未初始化局部缓冲区更新输出。48位写入只保存低48位，不报告高16位被舍弃。大端／小端（Big Endian／Little Endian）指存储字节序，不依赖主机自身字节序。

> 译注——契约与源码：完整公共说明见[已有NVMEM接口](../storage/P013_NVMEM接口参考.md)，结构见[数据单元](../storage/P019_NVMEM数据单元结构.md)。本页保留源码可见的INTERNAL_HIDDEN标记与字段，标记是Doxygen展示控制，不代表C语言字段不存在。相对源码链接用于跟踪，未把本次滚动main与任意本地版本视为相同。

头文件相对定位：[include/zephyr/nvmem.h](../../../include/zephyr/nvmem.h)，关联实现／接口：[subsys/nvmem/nvmem.c](../../../subsys/nvmem/nvmem.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/nvmem.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/nvmem/nvmem.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译或执行存储写入、掉电、低功耗、非法参数及实板实验。

## 1.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../storage/P020_NVMEM公共头文件.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/devicetree/nvmem.h](P002_NVMEM设备树头文件参考.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [nvmem_cell](../storage/P019_NVMEM数据单元结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [nvmem_cell_read](../storage/P013_NVMEM接口参考.md#ga5db94733cecfd4b46dd87ee07128d58d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [nvmem_cell_write](../storage/P013_NVMEM接口参考.md#gaef749ffc4b49e2e37b489fab2d8fa6b4)
- [nvmem_cell_is_ready](../storage/P013_NVMEM接口参考.md#ga614cac8acc913cb2f7b62c2f0d625421)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [nvmem_cell_is_read_only](../storage/P013_NVMEM接口参考.md#gac8abd20a158e3c304c73d6cb7e8cc50a)
- [nvmem_cell_read_le16](../storage/P013_NVMEM接口参考.md#ga4fac111617d3a2a2affab26d239c91ea)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sys_get_le16](../byteorder_reference/P001_系统字节序头文件参考.md#a5c2c537b960a29bdd29133f902a67f6a)
- [nvmem_cell_read_be16](../storage/P013_NVMEM接口参考.md#ga8d0acdfeb984292616d0a5c8b90c37be)
- [sys_get_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a91fae25b12126c2b35d240f56866184d)
- [nvmem_cell_read_le32](../storage/P013_NVMEM接口参考.md#ga3929245cba736565c5d7f746b09147a4)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_get_le32](../byteorder_reference/P001_系统字节序头文件参考.md#aa7422f922db351d2da1d52195d43b8a4)
- [nvmem_cell_read_be32](../storage/P013_NVMEM接口参考.md#gacce8148eeac974048659efea2be2d9bf)
- [sys_get_be32](../byteorder_reference/P001_系统字节序头文件参考.md#a4db31229c7a8a80dace3870664b6442d)
- [nvmem_cell_read_le48](../storage/P013_NVMEM接口参考.md#ga405e1697ca3ff9c8f33a3fea5dc8ffdb)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [sys_get_le48](../byteorder_reference/P001_系统字节序头文件参考.md#a601c3cefbdfd8befa336339a87fd70fd)
- [nvmem_cell_read_be48](../storage/P013_NVMEM接口参考.md#gae0974ff5106a37609d218340aad758ff)
- [sys_get_be48](../byteorder_reference/P001_系统字节序头文件参考.md#acf0fa9761998529910e022b80126ff6b)
- [nvmem_cell_read_le64](../storage/P013_NVMEM接口参考.md#gaf61422106876ef0995d0e5e6ebda6bd5)
- [sys_get_le64](../byteorder_reference/P001_系统字节序头文件参考.md#a678b08370e157ce5eb7117832aa86408)
- [nvmem_cell_read_be64](../storage/P013_NVMEM接口参考.md#gabf0dc8224abaeec54537c84b4bf0aa9b)
- [sys_get_be64](../byteorder_reference/P001_系统字节序头文件参考.md#ad8e00ff5c0b9e394291936d1a570c215)
- [nvmem_cell_write_le16](../storage/P013_NVMEM接口参考.md#ga5846faeb71b80da68044229de943833b)
- [sys_put_le16](../byteorder_reference/P001_系统字节序头文件参考.md#af8f30219c861bb07d097374204d386dd)
- [nvmem_cell_write_be16](../storage/P013_NVMEM接口参考.md#ga43e38af86b79d9ae5d9933e95fbbb134)
- [sys_put_be16](../byteorder_reference/P001_系统字节序头文件参考.md#a68df8f14dfc0d8715d16ac87dd4c73d2)
- [nvmem_cell_write_le32](../storage/P013_NVMEM接口参考.md#ga2ff30423cff4e064ab22cc13ff2fd60a)
- [sys_put_le32](../byteorder_reference/P001_系统字节序头文件参考.md#aff60d0dcda6a48df4ea248f898a92de0)
- [nvmem_cell_write_be32](../storage/P013_NVMEM接口参考.md#ga8e4eca68269a125baa5ae1bd6813a50a)
- [sys_put_be32](../byteorder_reference/P001_系统字节序头文件参考.md#a21f25ff68591217034f3414594425286)
- [nvmem_cell_write_le48](../storage/P013_NVMEM接口参考.md#ga377f8afd53d1d84e630de96a3620c13a)
- [sys_put_le48](../byteorder_reference/P001_系统字节序头文件参考.md#aa6950654cc7fd67ab4f83235da59665a)
- [nvmem_cell_write_be48](../storage/P013_NVMEM接口参考.md#ga1c119e9ad5817f47a6b99aaebc492da8)
- [sys_put_be48](../byteorder_reference/P001_系统字节序头文件参考.md#abe8d617e8a5469c303a512fe94a55443)
- [nvmem_cell_write_le64](../storage/P013_NVMEM接口参考.md#gac882709f9a2f8dcd4f48119cc73db3bd)
- [sys_put_le64](../byteorder_reference/P001_系统字节序头文件参考.md#a7d89d4b4b278fefa3e65fc6c3894a70c)
- [nvmem_cell_write_be64](../storage/P013_NVMEM接口参考.md#ga495e06601cfc7d7f41d3b16a58476b67)
- [sys_put_be64](../byteorder_reference/P001_系统字节序头文件参考.md#a3e0d2e4e85249497011f5f9ea0d2987c)

---

[返回大纲](大纲.md) · [下一章](P002_NVMEM设备树头文件参考.md)
