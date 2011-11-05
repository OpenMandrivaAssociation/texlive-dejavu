# revision 23969
# category Package
# catalog-ctan /fonts/dejavu
# catalog-date 2011-08-25 23:27:03 +0200
# catalog-license lppl
# catalog-version 2.33
Name:		texlive-dejavu
Version:	2.33
Release:	1
Summary:	LaTeX support for the fonts DejaVu
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dejavu
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package contains LaTeX support for the fonts DejaVu. They
are derived from the Vera fonts and contain more characters and
styles. The fonts are included in the original TrueType format
and converted Type 1 format. The (currently) supported
encodings are: OT1, T1, IL2, TS1, T2*, X2, QX, and LGR. The
package doesn't (currently) support math. More encodings and/or
features will come later.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-Italic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-Italic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed.afm
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_x2.enc
%{_texmfdistdir}/fonts/map/dvips/dejavu/dejavu-truetype.map
%{_texmfdistdir}/fonts/map/dvips/dejavu/dejavu-type1.map
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-x2.tfm
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-BoldOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-Oblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-BoldOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-Oblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-BoldOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-Oblique.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed.ttf
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Bold.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-BoldOblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Oblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Bold.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-BoldOblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Oblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Bold.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-BoldOblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Oblique.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Bold.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-BoldItalic.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Italic.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Bold.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-BoldItalic.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Italic.pfm
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed.pfm
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSans.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSansCondensed.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSansMono.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSerif.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSerifCondensed.sty
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/dejavu.sty
%doc %{_texmfdistdir}/doc/fonts/dejavu/CHANGELOG
%doc %{_texmfdistdir}/doc/fonts/dejavu/README
%doc %{_texmfdistdir}/doc/fonts/dejavu/dejavu-sample.pdf
%doc %{_texmfdistdir}/doc/fonts/dejavu/dejavu-sample.tex
%doc %{_texmfdistdir}/doc/fonts/dejavu/dejavu.pdf
%doc %{_texmfdistdir}/doc/fonts/dejavu/dejavu.tex
%doc %{_texmfdistdir}/doc/fonts/dejavu/extrakerns.zip
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/AUTHORS
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/BUGS
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/LICENSE
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/NEWS
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/README
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/langcover.txt
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/status.txt
%doc %{_texmfdistdir}/doc/fonts/dejavu/font-doc/unicover.txt
%doc %{_texmfdistdir}/doc/fonts/dejavu/manifest.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
