%global tl_name ucsmonograph
%global tl_revision 52698

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.0
Release:	%{tl_revision}.1
Summary:	Typesetting academic documents from the University of Caxias do Sul
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucsmonograph
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX class for typesetting academic documents according to
the ABNT (Brazilian Technical Standards Association) standards and the
UCS (University of Caxias do Sul) specifications.

