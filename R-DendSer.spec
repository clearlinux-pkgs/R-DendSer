#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DendSer
Version  : 1.0.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/DendSer_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DendSer_1.0.1.tar.gz
Summary  : Dendrogram seriation: ordering for visualisation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-DendSer-lib
Requires: R-gclus
Requires: R-seriation
BuildRequires : R-gclus
BuildRequires : R-seriation
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-DendSer package.
Group: Libraries

%description lib
lib components for the R-DendSer package.


%prep
%setup -q -c -n DendSer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299631

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523299631
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DendSer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DendSer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DendSer
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library DendSer|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DendSer/DESCRIPTION
/usr/lib64/R/library/DendSer/INDEX
/usr/lib64/R/library/DendSer/Meta/Rd.rds
/usr/lib64/R/library/DendSer/Meta/demo.rds
/usr/lib64/R/library/DendSer/Meta/features.rds
/usr/lib64/R/library/DendSer/Meta/hsearch.rds
/usr/lib64/R/library/DendSer/Meta/links.rds
/usr/lib64/R/library/DendSer/Meta/nsInfo.rds
/usr/lib64/R/library/DendSer/Meta/package.rds
/usr/lib64/R/library/DendSer/NAMESPACE
/usr/lib64/R/library/DendSer/R/DendSer
/usr/lib64/R/library/DendSer/R/DendSer.rdb
/usr/lib64/R/library/DendSer/R/DendSer.rdx
/usr/lib64/R/library/DendSer/demo/fib.R
/usr/lib64/R/library/DendSer/demo/pottery.R
/usr/lib64/R/library/DendSer/demo/sleep.R
/usr/lib64/R/library/DendSer/demo/toy.R
/usr/lib64/R/library/DendSer/help/AnIndex
/usr/lib64/R/library/DendSer/help/DendSer.rdb
/usr/lib64/R/library/DendSer/help/DendSer.rdx
/usr/lib64/R/library/DendSer/help/aliases.rds
/usr/lib64/R/library/DendSer/help/paths.rds
/usr/lib64/R/library/DendSer/html/00Index.html
/usr/lib64/R/library/DendSer/html/R.css
/usr/lib64/R/library/DendSer/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/DendSer/libs/DendSer.so
/usr/lib64/R/library/DendSer/libs/DendSer.so.avx2
/usr/lib64/R/library/DendSer/libs/DendSer.so.avx512
