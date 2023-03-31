Name:		texlive-ucsmonograph
Version:	52698
Release:	2
Summary:	Typesetting academic documents from the University of Caxias do Sul
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucsmonograph
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucsmonograph.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX class for typesetting academic documents
according to the ABNT (Brazilian Technical Standards
Association) standards and the UCS (University of Caxias do
Sul) specifications.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ucsmonograph
%{_texmfdistdir}/tex/latex/ucsmonograph
%doc %{_texmfdistdir}/doc/latex/ucsmonograph

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
