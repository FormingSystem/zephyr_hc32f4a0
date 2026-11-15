---
id: learning.zephyr-docs.api-source-reference.page-221
title: elf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第221章\_elf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html)。

## 221.1\_原始可见代码（Source Code）

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
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="foldopen00245"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00366"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="foldopen00378"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00404"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="l00473"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="agroup__llext__elf_html_ga1325c85290908b89a9c2b9bdd1aa2efd"></a>
<a id="agroup__llext__elf_html_ga141d58f50804ef53e0d9bd13fcb36424"></a>
<a id="agroup__llext__elf_html_ga144fdcc270b75a371880da097968555e"></a>
<a id="agroup__llext__elf_html_ga25ad092196ba8d073be66dc7629f8bc3"></a>
<a id="agroup__llext__elf_html_ga31413d6e89616f2d0356abd533b0c5a1"></a>
<a id="agroup__llext__elf_html_ga3358e1392fd861af8a7c8248519717a0"></a>
<a id="agroup__llext__elf_html_ga3e687a252b2bb6ed11ea9bc2fa6b728e"></a>
<a id="agroup__llext__elf_html_ga42c555ace34b21c1773c9e59228e9929"></a>
<a id="agroup__llext__elf_html_ga55f1dc601c95381307fddd5969969634"></a>
<a id="agroup__llext__elf_html_ga68e4179ac3b1c52c28c6e3e5c2a1838a"></a>
<a id="agroup__llext__elf_html_ga7f982d835a34713a84907873f9e058a9"></a>
<a id="agroup__llext__elf_html_ga9f98ad5b44106cacfd013f43f29a2eff"></a>
<a id="agroup__llext__elf_html_gaabf3a740e51b02fbaf40bedfba35e476"></a>
<a id="agroup__llext__elf_html_gab3695edd628cf868dc4f0d618f86bcbd"></a>
<a id="agroup__llext__elf_html_gab39a1763256a6b9ccccf8b89836cd192"></a>
<a id="agroup__llext__elf_html_gabb40eb5ffbe88010885da1c8c7b869e3"></a>
<a id="agroup__llext__elf_html_gac786571f50a02299b19c1a16d658ea72"></a>
<a id="agroup__llext__elf_html_gacb3487f81221d562af45632df161c64e"></a>
<a id="agroup__llext__elf_html_gad5c63f362ef6b26db73c37980d731c93"></a>
<a id="agroup__llext__elf_html_gad5dd8960a2fbfc74cdcd016b5c2c7cea"></a>
<a id="agroup__llext__elf_html_gae407130db14180c6737390604ba7c1fe"></a>
<a id="agroup__llext__elf_html_gafdcf88be776ec490cf1ec7c286f6202f"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructelf32__ehdr_html"></a>
<a id="astructelf32__ehdr_html_a085432a071a923e4fe1d3a4a3dfa665b"></a>
<a id="astructelf32__ehdr_html_a09a134b6c6b711458673ddc8601af4c5"></a>
<a id="astructelf32__ehdr_html_a0deea8c06b17aff924a86adf23206dd7"></a>
<a id="astructelf32__ehdr_html_a1533636f5162a1f5a6e501a4129a5954"></a>
<a id="astructelf32__ehdr_html_a2322a1ac85ac7962cd05152588f8bf8f"></a>
<a id="astructelf32__ehdr_html_a24ad42f294e548d54ff91ae9de5bb729"></a>
<a id="astructelf32__ehdr_html_a2b8ae6d098c44146579dbe4c8e2d11c8"></a>
<a id="astructelf32__ehdr_html_a33698f57f4f73a4f7659633fc11114fb"></a>
<a id="astructelf32__ehdr_html_a4537e3831f136b81a7a0d6260ad497a6"></a>
<a id="astructelf32__ehdr_html_a4f73aa6711f379fb70a483e99d47f108"></a>
<a id="astructelf32__ehdr_html_a5f795d38ed810bad582d88c35b474cbf"></a>
<a id="astructelf32__ehdr_html_acef0ea640d4fd75562b7412eaf8e2226"></a>
<a id="astructelf32__ehdr_html_ae26a4d5cc90917ec13689060695833e5"></a>
<a id="astructelf32__ehdr_html_af25dd95c6c2b2e8aeecdfb130ed4bfc6"></a>
<a id="astructelf32__rel_html"></a>
<a id="astructelf32__rel_html_a2bea1d7ef2a0c148cd9ae21386721f40"></a>
<a id="astructelf32__rel_html_ac93ab16d071b87719651f517893bba97"></a>
<a id="astructelf32__rela_html"></a>
<a id="astructelf32__rela_html_a37fce330c497dba2ca15c69cc58b83b8"></a>
<a id="astructelf32__rela_html_a4c3494d4b7abfec309895dff1891a466"></a>
<a id="astructelf32__rela_html_a4ef1961410f1b9ffea15615e03b3917b"></a>
<a id="astructelf32__shdr_html"></a>
<a id="astructelf32__shdr_html_a2f5302ddbc6ae2e7adc9d0747029ac07"></a>
<a id="astructelf32__shdr_html_a397da5153b2f7605b1ff1de6aefa6d72"></a>
<a id="astructelf32__shdr_html_a575fd441213a3a2c01a2b9f8d76ae91a"></a>
<a id="astructelf32__shdr_html_a812f8d63ce30897a2aafc8eecca004af"></a>
<a id="astructelf32__shdr_html_a99ef99ad56321d429d78a0d51fa55bc5"></a>
<a id="astructelf32__shdr_html_aa01fa67d235a73d8f05a1082ff639825"></a>
<a id="astructelf32__shdr_html_ab0d2f72391dd49af989bc4a96320e510"></a>
<a id="astructelf32__shdr_html_ac7185a5c368b86d7c5bde4261472d3ea"></a>
<a id="astructelf32__shdr_html_af97a639e2da493a81e104447e327b574"></a>
<a id="astructelf32__shdr_html_afc854954cb010c23281293399a58c200"></a>
<a id="astructelf32__sym_html"></a>
<a id="astructelf32__sym_html_a03dbc7e19d4f2f9aac76bf99d218658b"></a>
<a id="astructelf32__sym_html_a14545ec8738f87d6ac8da1d4a601d024"></a>
<a id="astructelf32__sym_html_a39b94d141bae73d0c1d8f6df5695ea2d"></a>
<a id="astructelf32__sym_html_a5ce8408912eda365e2e3246f81f98360"></a>
<a id="astructelf32__sym_html_aeef86f71df370cf183e2d03afe4d8812"></a>
<a id="astructelf32__sym_html_aef3af325acfa8080431f06de9267c662"></a>
<a id="astructelf64__ehdr_html"></a>
<a id="astructelf64__ehdr_html_a26fa9b30280c40d71227cd8dc68cc042"></a>
<a id="astructelf64__ehdr_html_a3566424cae4237c11dc781929e9d2396"></a>
<a id="astructelf64__ehdr_html_a419a672788fb33eaffc5f7eb7c9f9acd"></a>
<a id="astructelf64__ehdr_html_a4a3b62575f891b59851b36f478e95c32"></a>
<a id="astructelf64__ehdr_html_a6214fd0ea2f0d3e8151a304d5c4302b2"></a>
<a id="astructelf64__ehdr_html_a688f9d25b4f2678f0e9a313a8c8cf074"></a>
<a id="astructelf64__ehdr_html_a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9"></a>
<a id="astructelf64__ehdr_html_a7ee0e5959ca93262320c545a4ab11649"></a>
<a id="astructelf64__ehdr_html_a8d406a8c636ad09b96af62001b9b1785"></a>
<a id="astructelf64__ehdr_html_aa30814b4908ab8f0008f8b6a68686127"></a>
<a id="astructelf64__ehdr_html_ab41df1d736aabf7b810339d579e51663"></a>
<a id="astructelf64__ehdr_html_ac1c3b8c0f2b01d0edf07c0e3d1d8220b"></a>
<a id="astructelf64__ehdr_html_acfc6d7c908c9a9864cca2eb0e5a2c023"></a>
<a id="astructelf64__ehdr_html_ad46c9c2047e61617d5d52394e9c42d65"></a>
<a id="astructelf64__rel_html"></a>
<a id="astructelf64__rel_html_a4fdfdc207826e470ba8affcdf149acc9"></a>
<a id="astructelf64__rel_html_aa861a3f29f7bd9a78d527de69baba00c"></a>
<a id="astructelf64__rela_html"></a>
<a id="astructelf64__rela_html_a3eda7390faab39b1974174cc839cfb22"></a>
<a id="astructelf64__rela_html_a5fd82462e8b9c0eeaf84a00bc2aae3a4"></a>
<a id="astructelf64__rela_html_aa58223032a48222e420b36b2fc5f27ab"></a>
<a id="astructelf64__shdr_html"></a>
<a id="astructelf64__shdr_html_a283192781f8777274e0ed155b8caa52b"></a>
<a id="astructelf64__shdr_html_a41f5b8340cd4cb90b14cba348684d73b"></a>
<a id="astructelf64__shdr_html_a437c734872924c69bf3ea02723bfb50c"></a>
<a id="astructelf64__shdr_html_a58c125037ae69e35f1f18c3e7aeef222"></a>
<a id="astructelf64__shdr_html_a855b2f814e5b1127f3766ae44b1ded10"></a>
<a id="astructelf64__shdr_html_a978b62673b2b26f9d6333f0a3ccd7cb2"></a>
<a id="astructelf64__shdr_html_ab2d5b6d2b41c4b956917d2206b804335"></a>
<a id="astructelf64__shdr_html_abd91eb8261ee67e50232e3682dc43267"></a>
<a id="astructelf64__shdr_html_adf7c73f78f13d52220246e1ae6f99129"></a>
<a id="astructelf64__shdr_html_af58da5c7c3e7712c51396eb937e1e783"></a>
<a id="astructelf64__sym_html"></a>
<a id="astructelf64__sym_html_a285d9d47f979f7c0a3ae9ed18408d191"></a>
<a id="astructelf64__sym_html_a3037b0fbaf250e2e711ed5ad6b39fc88"></a>
<a id="astructelf64__sym_html_a47a54908caddb43875d6a167bec370c7"></a>
<a id="astructelf64__sym_html_a48d593f11ef3d04b1f5d46f92aaa9839"></a>
<a id="astructelf64__sym_html_a73ba49c8bee2c11229f48756dccea886"></a>
<a id="astructelf64__sym_html_aee1394841b7752ed58b47da46f83c0a5"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 * Copyright (c) 2024 Schneider Electric
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */
#ifndef ZEPHYR_INCLUDE_LLEXT_ELF_H_
#define ZEPHYR_INCLUDE_LLEXT_ELF_H_

#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif

typedef uint32_t elf32_addr;
typedef uint16_t elf32_half;
typedef uint32_t elf32_off;
typedef int32_t elf32_sword;
typedef uint32_t elf32_word;

typedef uint64_t elf64_addr;
typedef uint16_t elf64_half;
typedef uint64_t elf64_off;
typedef int32_t elf64_sword;
typedef uint32_t elf64_word;
typedef int64_t elf64_sxword;
typedef uint64_t elf64_xword;


#define EI_NIDENT 16

struct elf32_ehdr {
        unsigned char e_ident[EI_NIDENT];
        elf32_half e_type;
        elf32_half e_machine;
        elf32_word e_version;
        elf32_addr e_entry;
        elf32_off e_phoff;
        elf32_off e_shoff;
        elf32_word e_flags;
        elf32_half e_ehsize;
        elf32_half e_phentsize;
        elf32_half e_phnum;
        elf32_half e_shentsize;
        elf32_half e_shnum;
        elf32_half e_shstrndx;
};

struct elf64_ehdr {
        unsigned char e_ident[EI_NIDENT];
        elf64_half e_type;
        elf64_half e_machine;
        elf64_word e_version;
        elf64_addr e_entry;
        elf64_off e_phoff;
        elf64_off e_shoff;
        elf64_word e_flags;
        elf64_half e_ehsize;
        elf64_half e_phentsize;
        elf64_half e_phnum;
        elf64_half e_shentsize;
        elf64_half e_shnum;
        elf64_half e_shstrndx;
};

#define ET_REL  1

#define ET_EXEC 2

#define ET_DYN  3

#define ET_CORE 4

struct elf32_shdr {
        elf32_word sh_name;
        elf32_word sh_type;
        elf32_word sh_flags;
        elf32_addr sh_addr;
        elf32_off sh_offset;
        elf32_word sh_size;
        elf32_word sh_link;
        elf32_word sh_info;
        elf32_word sh_addralign;
        elf32_word sh_entsize;
};

struct elf64_shdr {
        elf64_word sh_name;
        elf64_word sh_type;
        elf64_xword sh_flags;
        elf64_addr sh_addr;
        elf64_off sh_offset;
        elf64_xword sh_size;
        elf64_word sh_link;
        elf64_word sh_info;
        elf64_xword sh_addralign;
        elf64_xword sh_entsize;
};

#define SHT_NULL 0x0
#define SHT_PROGBITS 0x1
#define SHT_SYMTAB 0x2
#define SHT_STRTAB 0x3
#define SHT_RELA 0x4
#define SHT_NOBITS 0x8
#define SHT_REL 0x9
#define SHT_DYNSYM 0xB
#define SHT_INIT_ARRAY 0xe
#define SHT_FINI_ARRAY 0xf
#define SHT_PREINIT_ARRAY 0x10

#define SHF_WRITE 0x1
#define SHF_ALLOC 0x2
#define SHF_EXECINSTR 0x4
#define SHF_TLS 0x400
#define SHF_MASKOS 0x0ff00000
#define SHF_LLEXT_HAS_RELOCS 0x00100000

#define SHF_BASIC_TYPE_MASK     (SHF_WRITE | SHF_ALLOC | SHF_EXECINSTR)

struct elf32_sym {
        elf32_word st_name;
        elf32_addr st_value;
        elf32_word st_size;
        unsigned char st_info;
        unsigned char st_other;
        elf32_half st_shndx;
};

struct elf64_sym {
        elf64_word st_name;
        unsigned char st_info;
        unsigned char st_other;
        elf64_half st_shndx;
        elf64_addr st_value;
        elf64_xword st_size;
};

#define SHN_UNDEF 0
#define SHN_LORESERVE 0xff00
#define SHN_ABS 0xfff1
#define SHN_COMMON 0xfff2
#define SHN_HIRESERVE 0xffff

#define STT_NOTYPE 0
#define STT_OBJECT 1
#define STT_FUNC 2
#define STT_SECTION 3
#define STT_FILE 4
#define STT_COMMON 5
#define STT_LOOS 10
#define STT_HIOS 12
#define STT_LOPROC 13
#define STT_HIPROC 15

#define STB_LOCAL 0
#define STB_GLOBAL 1
#define STB_WEAK 2
#define STB_LOOS 10
#define STB_HIOS 12
#define STB_LOPROC 13
#define STB_HIPROC 15

#define ELF32_ST_BIND(i) ((i) >> 4)

#define ELF32_ST_TYPE(i) ((i) & 0xf)

#define ELF64_ST_BIND(i) ((i) >> 4)


#define ELF64_ST_TYPE(i) ((i) & 0xf)

struct elf32_rel {
        elf32_addr r_offset;
        elf32_word r_info;
};

struct elf32_rela {
        elf32_addr r_offset;
        elf32_word r_info;
        elf32_sword r_addend;
};

#define ELF32_R_SYM(i) ((i) >> 8)

#define ELF32_R_TYPE(i) ((i) & 0xff)

struct elf64_rel {
        elf64_addr r_offset;
        elf64_xword r_info;
};

struct elf64_rela {
        elf64_addr r_offset;
        elf64_xword r_info;
        elf64_sxword r_addend;
};

#define ELF64_R_SYM(i) ((i) >> 32)

#define ELF64_R_TYPE(i) ((i) & 0xffffffff)


struct elf32_phdr {
        elf32_word p_type;
        elf32_off p_offset;
        elf32_addr p_vaddr;
        elf32_addr p_paddr;
        elf32_word p_filesz;
        elf32_word p_memsz;
        elf32_word p_flags;
        elf32_word p_align;
};

struct elf64_phdr {
        elf64_word p_type;
        elf64_off p_offset;
        elf64_addr p_vaddr;
        elf64_addr p_paddr;
        elf64_xword p_filesz;
        elf64_xword p_memsz;
        elf64_word p_flags;
        elf64_xword p_align;
};

#define PT_LOAD 1

struct elf32_dyn {
        elf32_sword d_tag;
        union {
                elf32_word d_val;
                elf32_addr d_ptr;
        } d_un;
};

struct elf64_dyn {
        elf64_sxword d_tag;
        union {
                elf64_xword d_val;
                elf64_addr d_ptr;
        } d_un;
};

#if defined(CONFIG_64BIT) || defined(__DOXYGEN__)
typedef struct elf64_ehdr elf_ehdr_t;
typedef struct elf64_shdr elf_shdr_t;
typedef struct elf64_phdr elf_phdr_t;
typedef elf64_addr elf_addr;
typedef elf64_half elf_half;
typedef elf64_xword elf_word;
typedef struct elf64_rel elf_rel_t;
typedef struct elf64_rela elf_rela_t;
typedef struct elf64_sym elf_sym_t;
#define ELF_R_SYM ELF64_R_SYM
#define ELF_R_TYPE ELF64_R_TYPE
#define ELF_ST_BIND ELF64_ST_BIND
#define ELF_ST_TYPE ELF64_ST_TYPE
#else
typedef struct elf32_ehdr elf_ehdr_t;
typedef struct elf32_shdr elf_shdr_t;
typedef struct elf32_phdr elf_phdr_t;
typedef elf32_addr elf_addr;
typedef elf32_half elf_half;
typedef elf32_word elf_word;
typedef struct elf32_rel elf_rel_t;
typedef struct elf32_rela elf_rela_t;
typedef struct elf32_sym elf_sym_t;
#define ELF_R_SYM ELF32_R_SYM
#define ELF_R_TYPE ELF32_R_TYPE
#define ELF_ST_BIND ELF32_ST_BIND
#define ELF_ST_TYPE ELF32_ST_TYPE
#endif

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_LLEXT_ELF_H_ */
```

## 221.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

版权（Copyright）：© 2024 Schneider Electric。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 525 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_ELF_H_`。

## 221.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)
- [elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [elf32_sword](../llext/P012_ELF常量与类型.md#ga1325c85290908b89a9c2b9bdd1aa2efd)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)
- [elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)
- [elf64_sword](../llext/P012_ELF常量与类型.md#ga31413d6e89616f2d0356abd533b0c5a1)
- [elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [elf64_sxword](../llext/P012_ELF常量与类型.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)
- [elf32_ehdr](../system_service_model_reference/P016_elf32_ehdr_结构体.md)
- [e_ident](../system_service_model_reference/P016_elf32_ehdr_结构体.md#acef0ea640d4fd75562b7412eaf8e2226)
- [EI_NIDENT](../llext/P012_ELF常量与类型.md#gae407130db14180c6737390604ba7c1fe)
- [e_type](../system_service_model_reference/P016_elf32_ehdr_结构体.md#ae26a4d5cc90917ec13689060695833e5)
- [e_machine](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a09a134b6c6b711458673ddc8601af4c5)
- [e_version](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a4f73aa6711f379fb70a483e99d47f108)
- [e_entry](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a2322a1ac85ac7962cd05152588f8bf8f)
- [e_phoff](../system_service_model_reference/P016_elf32_ehdr_结构体.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6)
- [e_shoff](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a085432a071a923e4fe1d3a4a3dfa665b)
- [e_flags](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a1533636f5162a1f5a6e501a4129a5954)
- [e_ehsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a33698f57f4f73a4f7659633fc11114fb)
- [e_phentsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a0deea8c06b17aff924a86adf23206dd7)
- [e_phnum](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a24ad42f294e548d54ff91ae9de5bb729)
- [e_shentsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a2b8ae6d098c44146579dbe4c8e2d11c8)
- [e_shnum](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a5f795d38ed810bad582d88c35b474cbf)
- [e_shstrndx](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a4537e3831f136b81a7a0d6260ad497a6)
- [elf64_ehdr](../system_service_model_reference/P021_elf64_ehdr_结构体.md)
- [e_ident](../system_service_model_reference/P021_elf64_ehdr_结构体.md#acfc6d7c908c9a9864cca2eb0e5a2c023)
- [e_type](../system_service_model_reference/P021_elf64_ehdr_结构体.md#aa30814b4908ab8f0008f8b6a68686127)
- [e_machine](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)
- [e_version](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a8d406a8c636ad09b96af62001b9b1785)
- [e_entry](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a26fa9b30280c40d71227cd8dc68cc042)
- [e_phoff](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ab41df1d736aabf7b810339d579e51663)
- [e_shoff](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a3566424cae4237c11dc781929e9d2396)
- [e_flags](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)
- [e_ehsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a7ee0e5959ca93262320c545a4ab11649)
- [e_phentsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a688f9d25b4f2678f0e9a313a8c8cf074)
- [e_phnum](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a4a3b62575f891b59851b36f478e95c32)
- [e_shentsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a419a672788fb33eaffc5f7eb7c9f9acd)
- [e_shnum](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ad46c9c2047e61617d5d52394e9c42d65)
- [e_shstrndx](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a6214fd0ea2f0d3e8151a304d5c4302b2)
- [elf32_shdr](../system_service_model_reference/P019_elf32_shdr_结构体.md)
- [sh_name](../system_service_model_reference/P019_elf32_shdr_结构体.md#a397da5153b2f7605b1ff1de6aefa6d72)
- [sh_type](../system_service_model_reference/P019_elf32_shdr_结构体.md#a575fd441213a3a2c01a2b9f8d76ae91a)
- [sh_flags](../system_service_model_reference/P019_elf32_shdr_结构体.md#a812f8d63ce30897a2aafc8eecca004af)
- [sh_addr](../system_service_model_reference/P019_elf32_shdr_结构体.md#a2f5302ddbc6ae2e7adc9d0747029ac07)
- [sh_offset](../system_service_model_reference/P019_elf32_shdr_结构体.md#ac7185a5c368b86d7c5bde4261472d3ea)
- [sh_size](../system_service_model_reference/P019_elf32_shdr_结构体.md#a99ef99ad56321d429d78a0d51fa55bc5)
- [sh_link](../system_service_model_reference/P019_elf32_shdr_结构体.md#afc854954cb010c23281293399a58c200)
- [sh_info](../system_service_model_reference/P019_elf32_shdr_结构体.md#aa01fa67d235a73d8f05a1082ff639825)
- [sh_addralign](../system_service_model_reference/P019_elf32_shdr_结构体.md#ab0d2f72391dd49af989bc4a96320e510)
- [sh_entsize](../system_service_model_reference/P019_elf32_shdr_结构体.md#af97a639e2da493a81e104447e327b574)
- [elf64_shdr](../system_service_model_reference/P024_elf64_shdr_结构体.md)
- [sh_name](../system_service_model_reference/P024_elf64_shdr_结构体.md#af58da5c7c3e7712c51396eb937e1e783)
- [sh_type](../system_service_model_reference/P024_elf64_shdr_结构体.md#adf7c73f78f13d52220246e1ae6f99129)
- [sh_flags](../system_service_model_reference/P024_elf64_shdr_结构体.md#abd91eb8261ee67e50232e3682dc43267)
- [sh_addr](../system_service_model_reference/P024_elf64_shdr_结构体.md#a58c125037ae69e35f1f18c3e7aeef222)
- [sh_offset](../system_service_model_reference/P024_elf64_shdr_结构体.md#a855b2f814e5b1127f3766ae44b1ded10)
- [sh_size](../system_service_model_reference/P024_elf64_shdr_结构体.md#a283192781f8777274e0ed155b8caa52b)
- [sh_link](../system_service_model_reference/P024_elf64_shdr_结构体.md#a437c734872924c69bf3ea02723bfb50c)
- [sh_info](../system_service_model_reference/P024_elf64_shdr_结构体.md#ab2d5b6d2b41c4b956917d2206b804335)
- [sh_addralign](../system_service_model_reference/P024_elf64_shdr_结构体.md#a978b62673b2b26f9d6333f0a3ccd7cb2)
- [sh_entsize](../system_service_model_reference/P024_elf64_shdr_结构体.md#a41f5b8340cd4cb90b14cba348684d73b)
- [elf32_sym](../system_service_model_reference/P020_elf32_sym_结构体.md)
- [st_name](../system_service_model_reference/P020_elf32_sym_结构体.md#a14545ec8738f87d6ac8da1d4a601d024)
- [st_value](../system_service_model_reference/P020_elf32_sym_结构体.md#a39b94d141bae73d0c1d8f6df5695ea2d)
- [st_size](../system_service_model_reference/P020_elf32_sym_结构体.md#aef3af325acfa8080431f06de9267c662)
- [st_info](../system_service_model_reference/P020_elf32_sym_结构体.md#aeef86f71df370cf183e2d03afe4d8812)
- [st_other](../system_service_model_reference/P020_elf32_sym_结构体.md#a5ce8408912eda365e2e3246f81f98360)
- [st_shndx](../system_service_model_reference/P020_elf32_sym_结构体.md#a03dbc7e19d4f2f9aac76bf99d218658b)
- [elf64_sym](../system_service_model_reference/P025_elf64_sym_结构体.md)
- [st_name](../system_service_model_reference/P025_elf64_sym_结构体.md#aee1394841b7752ed58b47da46f83c0a5)
- [st_info](../system_service_model_reference/P025_elf64_sym_结构体.md#a48d593f11ef3d04b1f5d46f92aaa9839)
- [st_other](../system_service_model_reference/P025_elf64_sym_结构体.md#a47a54908caddb43875d6a167bec370c7)
- [st_shndx](../system_service_model_reference/P025_elf64_sym_结构体.md#a285d9d47f979f7c0a3ae9ed18408d191)
- [st_value](../system_service_model_reference/P025_elf64_sym_结构体.md#a3037b0fbaf250e2e711ed5ad6b39fc88)
- [st_size](../system_service_model_reference/P025_elf64_sym_结构体.md#a73ba49c8bee2c11229f48756dccea886)
- [elf32_rel](../system_service_model_reference/P017_elf32_rel_结构体.md)
- [r_offset](../system_service_model_reference/P017_elf32_rel_结构体.md#a2bea1d7ef2a0c148cd9ae21386721f40)
- [r_info](../system_service_model_reference/P017_elf32_rel_结构体.md#ac93ab16d071b87719651f517893bba97)
- [elf32_rela](../system_service_model_reference/P018_elf32_rela_结构体.md)
- [r_offset](../system_service_model_reference/P018_elf32_rela_结构体.md#a4ef1961410f1b9ffea15615e03b3917b)
- [r_info](../system_service_model_reference/P018_elf32_rela_结构体.md#a4c3494d4b7abfec309895dff1891a466)
- [r_addend](../system_service_model_reference/P018_elf32_rela_结构体.md#a37fce330c497dba2ca15c69cc58b83b8)
- [elf64_rel](../system_service_model_reference/P022_elf64_rel_结构体.md)
- [r_offset](../system_service_model_reference/P022_elf64_rel_结构体.md#a4fdfdc207826e470ba8affcdf149acc9)
- [r_info](../system_service_model_reference/P022_elf64_rel_结构体.md#aa861a3f29f7bd9a78d527de69baba00c)
- [elf64_rela](../system_service_model_reference/P023_elf64_rela_结构体.md)
- [r_offset](../system_service_model_reference/P023_elf64_rela_结构体.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4)
- [r_info](../system_service_model_reference/P023_elf64_rela_结构体.md#aa58223032a48222e420b36b2fc5f27ab)
- [r_addend](../system_service_model_reference/P023_elf64_rela_结构体.md#a3eda7390faab39b1974174cc839cfb22)
- [elf_ehdr_t](../llext/P012_ELF常量与类型.md#gab39a1763256a6b9ccccf8b89836cd192)
- [elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)
- [elf_phdr_t](../llext/P012_ELF常量与类型.md#gad5c63f362ef6b26db73c37980d731c93)
- [elf_addr](../llext/P012_ELF常量与类型.md#ga9f98ad5b44106cacfd013f43f29a2eff)
- [elf_half](../llext/P012_ELF常量与类型.md#gacb3487f81221d562af45632df161c64e)
- [elf_word](../llext/P012_ELF常量与类型.md#ga25ad092196ba8d073be66dc7629f8bc3)
- [elf_rel_t](../llext/P012_ELF常量与类型.md#gafdcf88be776ec490cf1ec7c286f6202f)
- [elf_rela_t](../llext/P012_ELF常量与类型.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)
- [elf_sym_t](../llext/P012_ELF常量与类型.md#ga144fdcc270b75a371880da097968555e)
- [elf32_ehdr::e_shoff](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a085432a071a923e4fe1d3a4a3dfa665b)
- [elf32_ehdr::e_machine](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a09a134b6c6b711458673ddc8601af4c5)
- [elf32_ehdr::e_phentsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a0deea8c06b17aff924a86adf23206dd7)
- [elf32_ehdr::e_flags](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a1533636f5162a1f5a6e501a4129a5954)
- [elf32_ehdr::e_entry](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a2322a1ac85ac7962cd05152588f8bf8f)
- [elf32_ehdr::e_phnum](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a24ad42f294e548d54ff91ae9de5bb729)
- [elf32_ehdr::e_shentsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a2b8ae6d098c44146579dbe4c8e2d11c8)
- [elf32_ehdr::e_ehsize](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a33698f57f4f73a4f7659633fc11114fb)
- [elf32_ehdr::e_shstrndx](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a4537e3831f136b81a7a0d6260ad497a6)
- [elf32_ehdr::e_version](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a4f73aa6711f379fb70a483e99d47f108)
- [elf32_ehdr::e_shnum](../system_service_model_reference/P016_elf32_ehdr_结构体.md#a5f795d38ed810bad582d88c35b474cbf)
- [elf32_ehdr::e_ident](../system_service_model_reference/P016_elf32_ehdr_结构体.md#acef0ea640d4fd75562b7412eaf8e2226)
- [elf32_ehdr::e_type](../system_service_model_reference/P016_elf32_ehdr_结构体.md#ae26a4d5cc90917ec13689060695833e5)
- [elf32_ehdr::e_phoff](../system_service_model_reference/P016_elf32_ehdr_结构体.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6)
- [elf32_rel::r_offset](../system_service_model_reference/P017_elf32_rel_结构体.md#a2bea1d7ef2a0c148cd9ae21386721f40)
- [elf32_rel::r_info](../system_service_model_reference/P017_elf32_rel_结构体.md#ac93ab16d071b87719651f517893bba97)
- [elf32_rela::r_addend](../system_service_model_reference/P018_elf32_rela_结构体.md#a37fce330c497dba2ca15c69cc58b83b8)
- [elf32_rela::r_info](../system_service_model_reference/P018_elf32_rela_结构体.md#a4c3494d4b7abfec309895dff1891a466)
- [elf32_rela::r_offset](../system_service_model_reference/P018_elf32_rela_结构体.md#a4ef1961410f1b9ffea15615e03b3917b)
- [elf32_shdr::sh_addr](../system_service_model_reference/P019_elf32_shdr_结构体.md#a2f5302ddbc6ae2e7adc9d0747029ac07)
- [elf32_shdr::sh_name](../system_service_model_reference/P019_elf32_shdr_结构体.md#a397da5153b2f7605b1ff1de6aefa6d72)
- [elf32_shdr::sh_type](../system_service_model_reference/P019_elf32_shdr_结构体.md#a575fd441213a3a2c01a2b9f8d76ae91a)
- [elf32_shdr::sh_flags](../system_service_model_reference/P019_elf32_shdr_结构体.md#a812f8d63ce30897a2aafc8eecca004af)
- [elf32_shdr::sh_size](../system_service_model_reference/P019_elf32_shdr_结构体.md#a99ef99ad56321d429d78a0d51fa55bc5)
- [elf32_shdr::sh_info](../system_service_model_reference/P019_elf32_shdr_结构体.md#aa01fa67d235a73d8f05a1082ff639825)
- [elf32_shdr::sh_addralign](../system_service_model_reference/P019_elf32_shdr_结构体.md#ab0d2f72391dd49af989bc4a96320e510)
- [elf32_shdr::sh_offset](../system_service_model_reference/P019_elf32_shdr_结构体.md#ac7185a5c368b86d7c5bde4261472d3ea)
- [elf32_shdr::sh_entsize](../system_service_model_reference/P019_elf32_shdr_结构体.md#af97a639e2da493a81e104447e327b574)
- [elf32_shdr::sh_link](../system_service_model_reference/P019_elf32_shdr_结构体.md#afc854954cb010c23281293399a58c200)
- [elf32_sym::st_shndx](../system_service_model_reference/P020_elf32_sym_结构体.md#a03dbc7e19d4f2f9aac76bf99d218658b)
- [elf32_sym::st_name](../system_service_model_reference/P020_elf32_sym_结构体.md#a14545ec8738f87d6ac8da1d4a601d024)
- [elf32_sym::st_value](../system_service_model_reference/P020_elf32_sym_结构体.md#a39b94d141bae73d0c1d8f6df5695ea2d)
- [elf32_sym::st_other](../system_service_model_reference/P020_elf32_sym_结构体.md#a5ce8408912eda365e2e3246f81f98360)
- [elf32_sym::st_info](../system_service_model_reference/P020_elf32_sym_结构体.md#aeef86f71df370cf183e2d03afe4d8812)
- [elf32_sym::st_size](../system_service_model_reference/P020_elf32_sym_结构体.md#aef3af325acfa8080431f06de9267c662)
- [elf64_ehdr::e_entry](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a26fa9b30280c40d71227cd8dc68cc042)
- [elf64_ehdr::e_shoff](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a3566424cae4237c11dc781929e9d2396)
- [elf64_ehdr::e_shentsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a419a672788fb33eaffc5f7eb7c9f9acd)
- [elf64_ehdr::e_phnum](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a4a3b62575f891b59851b36f478e95c32)
- [elf64_ehdr::e_shstrndx](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a6214fd0ea2f0d3e8151a304d5c4302b2)
- [elf64_ehdr::e_phentsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a688f9d25b4f2678f0e9a313a8c8cf074)
- [elf64_ehdr::e_flags](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)
- [elf64_ehdr::e_ehsize](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a7ee0e5959ca93262320c545a4ab11649)
- [elf64_ehdr::e_version](../system_service_model_reference/P021_elf64_ehdr_结构体.md#a8d406a8c636ad09b96af62001b9b1785)
- [elf64_ehdr::e_type](../system_service_model_reference/P021_elf64_ehdr_结构体.md#aa30814b4908ab8f0008f8b6a68686127)
- [elf64_ehdr::e_phoff](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ab41df1d736aabf7b810339d579e51663)
- [elf64_ehdr::e_machine](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)
- [elf64_ehdr::e_ident](../system_service_model_reference/P021_elf64_ehdr_结构体.md#acfc6d7c908c9a9864cca2eb0e5a2c023)
- [elf64_ehdr::e_shnum](../system_service_model_reference/P021_elf64_ehdr_结构体.md#ad46c9c2047e61617d5d52394e9c42d65)
- [elf64_rel::r_offset](../system_service_model_reference/P022_elf64_rel_结构体.md#a4fdfdc207826e470ba8affcdf149acc9)
- [elf64_rel::r_info](../system_service_model_reference/P022_elf64_rel_结构体.md#aa861a3f29f7bd9a78d527de69baba00c)
- [elf64_rela::r_addend](../system_service_model_reference/P023_elf64_rela_结构体.md#a3eda7390faab39b1974174cc839cfb22)
- [elf64_rela::r_offset](../system_service_model_reference/P023_elf64_rela_结构体.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4)
- [elf64_rela::r_info](../system_service_model_reference/P023_elf64_rela_结构体.md#aa58223032a48222e420b36b2fc5f27ab)
- [elf64_shdr::sh_size](../system_service_model_reference/P024_elf64_shdr_结构体.md#a283192781f8777274e0ed155b8caa52b)
- [elf64_shdr::sh_entsize](../system_service_model_reference/P024_elf64_shdr_结构体.md#a41f5b8340cd4cb90b14cba348684d73b)
- [elf64_shdr::sh_link](../system_service_model_reference/P024_elf64_shdr_结构体.md#a437c734872924c69bf3ea02723bfb50c)
- [elf64_shdr::sh_addr](../system_service_model_reference/P024_elf64_shdr_结构体.md#a58c125037ae69e35f1f18c3e7aeef222)
- [elf64_shdr::sh_offset](../system_service_model_reference/P024_elf64_shdr_结构体.md#a855b2f814e5b1127f3766ae44b1ded10)
- [elf64_shdr::sh_addralign](../system_service_model_reference/P024_elf64_shdr_结构体.md#a978b62673b2b26f9d6333f0a3ccd7cb2)
- [elf64_shdr::sh_info](../system_service_model_reference/P024_elf64_shdr_结构体.md#ab2d5b6d2b41c4b956917d2206b804335)
- [elf64_shdr::sh_flags](../system_service_model_reference/P024_elf64_shdr_结构体.md#abd91eb8261ee67e50232e3682dc43267)
- [elf64_shdr::sh_type](../system_service_model_reference/P024_elf64_shdr_结构体.md#adf7c73f78f13d52220246e1ae6f99129)
- [elf64_shdr::sh_name](../system_service_model_reference/P024_elf64_shdr_结构体.md#af58da5c7c3e7712c51396eb937e1e783)
- [elf64_sym::st_shndx](../system_service_model_reference/P025_elf64_sym_结构体.md#a285d9d47f979f7c0a3ae9ed18408d191)
- [elf64_sym::st_value](../system_service_model_reference/P025_elf64_sym_结构体.md#a3037b0fbaf250e2e711ed5ad6b39fc88)
- [elf64_sym::st_other](../system_service_model_reference/P025_elf64_sym_结构体.md#a47a54908caddb43875d6a167bec370c7)
- [elf64_sym::st_info](../system_service_model_reference/P025_elf64_sym_结构体.md#a48d593f11ef3d04b1f5d46f92aaa9839)
- [elf64_sym::st_size](../system_service_model_reference/P025_elf64_sym_结构体.md#a73ba49c8bee2c11229f48756dccea886)
- [elf64_sym::st_name](../system_service_model_reference/P025_elf64_sym_结构体.md#aee1394841b7752ed58b47da46f83c0a5)

---

[上一章](P220_edac_synopsys.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P222_emsdp-pinctrl.h_源码浏览.md)
