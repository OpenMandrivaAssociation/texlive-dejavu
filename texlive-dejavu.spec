%global tl_name dejavu
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.34
Release:	%{tl_revision}.1
Summary:	LaTeX support for the DejaVu fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dejavu
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains LaTeX support for the DejaVu fonts, which are
derived from the Vera fonts but contain more characters and styles. The
fonts are included in the original TrueType format, and in converted
Type 1 format. The (currently) supported encodings are: OT1, T1, IL2,
TS1, T2*, X2, QX, and LGR. The package doesn't (currently) support
mathematics. More encodings and/or features are expected.

